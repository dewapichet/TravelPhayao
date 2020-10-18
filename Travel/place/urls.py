from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Amphoe', views.GetAmphoe.as_view()),
    path('Place', views.GetPlace.as_view()),
]
