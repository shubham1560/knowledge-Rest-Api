from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Another(View):

    def get(self, request):
        return HttpResponse("Working with the class too")


def first(request):
    return HttpResponse("Working!" + str(request))


