from rest_framework import serializers
from .models import Amphoe, Place


class AmphoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amphoe
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
