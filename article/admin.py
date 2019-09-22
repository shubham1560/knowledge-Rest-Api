from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'active', 'created_on', 'parent_article', 'workflow_state', 'article_category')
    # fields = ['article_number', 'workflow_state']  # TO control fields that we can see in form
    list_filter = ['workflow_state', 'author', 'article_category']
    search_fields = ['topic']


admin.site.register(Article, ArticleAdmin)
