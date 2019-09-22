from rest_framework import serializers
from .models import Article, ArticleTag


class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ['id', 'tag']


class ArticleSerializer(serializers.ModelSerializer):
    tags = ArticleTagSerializer(many=False)  # should not conflict with field names in serializer

    class Meta:
        model = Article
        fields = ['id', 'topic', 'article_number', 'article_body', 'workflow_state', 'tags']
