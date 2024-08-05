from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, PasswordResetView, UserListView, UserDetailView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('user_list/', UserListView.as_view(template_name='user_list.html'), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(template_name='user_detail.html'), name='user-detail'),
    path('user/<int:pk>/update/', UserUpdateView.as_view(template_name='user_update.html'), name='user-update'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),

]