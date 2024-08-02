from django.views.generic import DetailView
from .models import Blog


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'article_detail.html'
    context_object_name = 'article'
