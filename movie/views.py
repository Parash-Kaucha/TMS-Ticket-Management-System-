from multiprocessing import context
from tkinter import S
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import generics
from movie.models import Movie, ShowTime, Studio
from movie.serializers import MovieSerializer, ShowTimeSerializer, StudioSerializer, AddShowTimeSerializer
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
# from rest_framework_simplejwt import JWTAuthentication
# Create your views here.

class StudioVeiwSet(ModelViewSet):
    serializer_class = StudioSerializer
    queryset = Studio.objects.all()
    # def post(self, request):
    #     data = request.data
    #     serializer=self.serializer_class(data=data)
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(data=serializer.errors)

    # def get(self, request):
    #     studio = Studio.objects.all()
    #     serializer = self.serializer_class(instance=studio, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    # def get(self, request):
    #     movies = Movie.objects.all()
    #     serializer = self.serializer_class(instance=movies, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     data = request.data

    #     serializer = self.serializer_class(data=data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(data=serializer.data)

    #     return Response(data=serializer.errors)

    # def get(self, request, movie_id):
    #     movie = get_object_or_404(Movie, pk=movie_id)

    #     serializer = self.serializer_class(instance=movie, many=True)

    #     return Response(data=serializer.data)


# class GetDetailListView(generics.GenericAPIView):
    # serializer_class = [StudioSerializer, MovieSerializer]
    # queryset = [Studio.objects.all(), Movie.objects.all()]
    # def get(self, request):

    #     studio = Studio.objects.all()

    #     serializer = self.serializer_class(instance=studio, many=True)

    #     return Response(data=serializer.data)

# @api_view(['get'])
# def get_movie_data(request):
#     movie_query = Movie.objects.all()
#     studio_query = Studio.objects.all()
#     movie_serializer = MovieSerializer(movie_query, many=True)
#     studio_serializer = StudioSerializer(studio_query, many=True)

#     final_data = {'movie':movie_serializer.data, 'studio':studio_serializer.data}

#     return JsonResponse(data=final_data, safe=True)

@api_view(['get'])
def get_details(request):
    movie_query = Movie.objects.all()
    studio_query = Studio.objects.all()
    queryset = movie_query and studio_query
    serializer = AddShowTimeSerializer(queryset, many=True)
    return Response(data=serializer.data, safe=True)

# class ShowTimeListView(generics.GenericAPIView):
#     serializer_class = serializers.ShowTimeSerializer
#     queryset = ShowTime.objects.all()
#     def get(self, request):
#         show_time = ShowTime.objects.all()
#         serializer = self.serializer_class(instance=show_time, many=True)
#         return Response(data=serializer.data)

class ShowTimeViewSet(ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer