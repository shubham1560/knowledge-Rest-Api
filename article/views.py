from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class AricleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)  # To restrict permission to this single model or viewSet

# class inheriting View already has many things configured for us but it makes the program complex


class Another(View):

    def get(self, request):
        articles = Article.objects.all()
        article_by_id = Article.objects.get(id=2)
        for article in articles:
            print(article.author)
            print(article.article_number)
        return HttpResponse("Working with " + article_by_id.article_number+" article")


def first(request):
    return HttpResponse("Working!" + str(request))


