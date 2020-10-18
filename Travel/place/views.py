from django.shortcuts import render
from rest_framework import generics
from .models import Amphoe, Place
from .serializers import AmphoeSerializer, PlaceSerializer

# Create your views here.

class GetAmphoe(generics.ListCreateAPIView):
    queryset = Amphoe.objects.all()
    serializer_class = AmphoeSerializer


class GetPlace(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


