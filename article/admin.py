from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'active', 'created_on', 'parent_article', 'workflow_state', 'article_category')


admin.site.register(Article, ArticleAdmin)
