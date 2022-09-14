from movie.models import Movie, ShowTime, Studio, TicketBooking
from movie.serializers import MovieSerializer, ShowTimeSerializer, StudioSerializer, TicketBookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)


class StudioVeiwSet(ModelViewSet):
    serializer_class = StudioSerializer
    queryset = Studio.objects.all()
    permission_classes = [IsAdminUser]

class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAdminUser]


class ShowTimeViewSet(ModelViewSet):
    queryset = ShowTime.objects.all()
    serializer_class = ShowTimeSerializer


class TicketBookingViewSet(ModelViewSet):
    queryset = TicketBooking.objects.all()
    serializer_class = TicketBookingSerializer
    permission_classes = [IsAuthenticated]