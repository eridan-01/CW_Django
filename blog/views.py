from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
