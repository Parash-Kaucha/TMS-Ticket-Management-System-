from django.contrib import admin
from .models import Movie, ShowTime, Studio
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
                    'movie_name',
                    'movie_length',
                    'movie_lang',
                    'movie_subtitle',
                    'movie_genre', 
                    'movie_director',
                    'movie_cast',
                    'movie_synopsis'
                    ]
                
@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = [
                    'studio_name',
                    'studio_capacity',
                    'available_seats'
                    ]

admin.site.register(ShowTime)