from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'views')
    search_fields = ('title', 'content')
    list_filter = ('publication_date',)
    ordering = ('-publication_date',)
