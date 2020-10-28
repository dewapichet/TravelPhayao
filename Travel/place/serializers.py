from rest_framework import serializers
from .models import Amphoe, Place, Trip


class AmphoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amphoe
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    Amphoe_data = AmphoeSerializer(read_only=True , source='Amphoe')
    class Meta:
        model = Place
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
