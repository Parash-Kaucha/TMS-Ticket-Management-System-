from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Movie, Studio, ShowTime
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
                    'movie_id',
                    'movie_name',
                    'movie_length',
                    'movie_starttime',
                    'movie_endtime',
                    'movie_lang',
                    'movie_subtitle',
                    'movie_genre', 
                    'movie_director',
                    'movie_cast',
                    'movie_synopsis'
                ]

class StudioSerializer(serializers.ModelSerializer):
    movie = serializers.HyperlinkedRelatedField(read_only=True, view_name='create_movie')
    class Meta:
        model = Studio
        # fields = [
        #             'movie',
        #             'studio_id',
        #             'studio_name',
        #             'studio_capacity',
        #             'available_seats'
        #         ]
        fields = '__all__'


class AddShowTimeSerializer(serializers.ModelSerializer):
    movies = MovieSerializer()
    studio = StudioSerializer()


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'