from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Movie, Studio, ShowTime, TicketBooking


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'


class TicketBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketBooking
        fields = '__all__'
        