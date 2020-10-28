from django.shortcuts import render
from rest_framework import generics
from .models import Amphoe, Place, Trip
from .serializers import AmphoeSerializer, PlaceSerializer, TripSerializer

# Create your views here.

class GetAmphoe(generics.ListCreateAPIView):
    queryset = Amphoe.objects.all()
    serializer_class = AmphoeSerializer


class GetPlace(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class GetIdPlace(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return  Place.objects.filter(Amphoe=self.kwargs['Amphoe'])

class GetIdPlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    lookup_field = 'id'
    serializer_class = PlaceSerializer

class GetTrip(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
