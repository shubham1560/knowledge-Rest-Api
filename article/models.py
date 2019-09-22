from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ArticleTag(models.Model):
    tag = models.CharField(max_length=50)


class Article(models.Model):

    WORKFLOW_STATES = (
        ('draft', 'Draft'),
        ('review', 'Review'),
        ('published', 'Published'),
        ('retired', 'Retired'),
        ('outdated', 'Outdated'),
    )

    CATEGORIES = (
        ('1', 'Tower'),
        ('2', 'Insurance'),
        ('3', 'Sales'),
    )

    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    article_number = models.CharField(max_length=10, unique=True)
    parent_article = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    workflow_state = models.CharField(max_length=20, choices=WORKFLOW_STATES)
    article_body = models.CharField(max_length=2000)
    article_category = models.CharField(max_length=1, choices=CATEGORIES)
    disable_commenting = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    topic = models.CharField(max_length=50)
    tags = models.OneToOneField(ArticleTag, blank=True, null=True, on_delete=models.CASCADE)


class ArticleUse(models.Model):
    comment = models.CharField(max_length=100)
    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                          related_name='articleUse')  # related serializer
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, )
    created_on = models.DateTimeField(auto_now=True)
