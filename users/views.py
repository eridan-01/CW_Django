import secrets
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm, UserModeratorForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserListView(LoginRequiredMixin, ListView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user-list')
    context_object_name = 'users'  # Имя, под которым список пользователей будет доступен в шаблоне
    extra_context = {'title': 'Пользователи'}

    def get_queryset(self):
        # Здесь можно настроить фильтрацию или сортировку, если нужно
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Вы можете добавить дополнительные данные в контекст, если нужно
        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user-list')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтверждение почты",
                  message=f"Перейдите по ссылке для подтверждения почты {url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'users/password_reset.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            new_password = generate_random_password()
            user.password = make_password(new_password)
            user.save()

            send_mail(
                subject='Восстановление пароля',
                message=f'Ваш новый пароль: {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )

            messages.success(request, 'Пароль успешно изменён. Пожалуйста, войдите с новым паролем.')

            return redirect('users:login')
        else:
            messages.error(request, 'Нет пользователя с таким email.')
            return redirect('users:password_reset')


@login_required
@permission_required('auth.block_user')
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect('user_list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    success_url = reverse_lazy('users:user-detail')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:user-list')

    def get_form_class(self):
        user = self.request.user
        if user.is_staff or user.groups.filter(name='managers').exists():
            return UserModeratorForm
        raise PermissionDenied

