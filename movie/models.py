from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Movie(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    movie_length = models.DecimalField(max_digits=3, decimal_places=2)
    movie_starttime = models.TimeField()
    movie_endtime = models.TimeField()
    movie_lang = models.CharField(max_length=100)
    movie_subtitle = models.BooleanField(default=False)
    movie_genre = models.CharField(max_length=200)
    movie_director = models.CharField(max_length=100)
    movie_cast = models.CharField(max_length=250)
    movie_synopsis = models.TextField(null=True)

    def __str__(self):
        return self.movie_name


class Studio(models.Model):
    studio_id = models.BigAutoField(primary_key=True)
    studio_name = models.CharField(max_length=30)
    studio_capacity = models.IntegerField(blank=False)
    available_seats = models.IntegerField(blank=False)

    def __str__(self):
        return self.studio_name


class ShowTime(models.Model):
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, related_name='studio')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class TicketBooking(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ShowTime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='showtime')
    seats = models.IntegerField(default=1)
    creation_time = models.DateTimeField(default=datetime.now())