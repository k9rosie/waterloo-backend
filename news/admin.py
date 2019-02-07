from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('title', 'article_authors', 'created_at')
    autocomplete_fields = ['authors']
    prepopulated_fields = {'slug': ('title',), }
