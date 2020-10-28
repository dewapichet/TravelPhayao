from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('Amphoe', views.GetAmphoe.as_view()),
    path('Place', views.GetPlace.as_view()),
    path('Place/<int:Amphoe>', views.GetIdPlace.as_view()),
    path('Place/Travel/<int:id>', views.GetIdPlaceDetail.as_view()),
    path('Trip', views.GetTrip.as_view())
]
