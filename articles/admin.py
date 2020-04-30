from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('author', 'published',)
    list_display = ('title', 'author', 'published')
    search_fields = ('author', 'title', 'body')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'body', 'author', 'published')
    
