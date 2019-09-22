from rest_framework import serializers
from .models import Article, ArticleTag, ArticleUse
from django.contrib.auth.models import User


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ['id', 'tag']


class ArticleUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleUse
        fields = ['id', 'comment', 'commented_by', 'commented_article']


class ArticleSerializer(serializers.ModelSerializer):
    tags = ArticleTagSerializer(many=False)  # should not conflict with field names in serializer
    articleUse = ArticleUseSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'topic', 'article_number', 'article_body', 'workflow_state', 'tags', 'articleUse', 'child',
                  'author']


class AuthorSerializer(serializers.ModelSerializer):
    author = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'author']
