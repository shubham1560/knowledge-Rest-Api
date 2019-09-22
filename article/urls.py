from django.urls import path, include
# from . import views
from .views import Another
from rest_framework import routers
from .views import AricleViewSet


router = routers.DefaultRouter()
router.register('articles', AricleViewSet)


urlpatterns = [
    # path('', views.first, name="home"),
    path('', include(router.urls)),
    path('classCall', Another.as_view()),
]
