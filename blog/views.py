from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {'title': 'Блог'}


class BlogDetailView(DetailView):
    model = Blog
