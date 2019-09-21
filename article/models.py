from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    created_on = models.DateTimeField()
    article_number = models.CharField(max_length=10)
    parent_article = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    workflow_state = models.CharField(max_length=20, choices=WORKFLOW_STATES)
    article_body = models.CharField(max_length=2000)
    article_category = models.CharField(max_length=1, choices=CATEGORIES)
    disable_commenting = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
