from django.urls import path, include
from . import views
from .views import Another

urlpatterns = [
    path('', views.first, name="home"),
    path('classCall', Another.as_view())
]
