from django.contrib import admin
from .models import Article, ArticleTag, ArticleUse
# ArticleView
#
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_number', 'active', 'created_on', 'parent_article', 'workflow_state', 'article_category')
    # fields = ['article_number', 'workflow_state']  # TO control fields that we can see in form
    list_filter = ['workflow_state', 'author', 'article_category']
    search_fields = ['topic']


class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


class ArticleUseAdmin(admin.ModelAdmin):
    list_display = ('id', 'commented_by', 'commented_article')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleTag, ArticleTagAdmin)
admin.site.register(ArticleUse, ArticleUseAdmin)
