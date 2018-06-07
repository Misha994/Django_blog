from django.contrib import admin
from .models import Article, Comments


class ArticleInLine(admin.StackedInline):
    model = Comments
    # The number of comments that are displayed for the default
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    # Add comments fields
    inlines = [ArticleInLine]
    # Filter for articles in Django administration
    list_filter = ['article_date']


# Gives administrator opportunity create article
admin.site.register(Article, ArticleAdmin)
