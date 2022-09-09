from django.contrib import admin
from django.urls import path, include
from movie import views

# router = DefaultRouter()

# router.register('movieapi', views.MovieModelViewSet, basename='movie')
# router.register('studioapi', views.StudioModelViewSet, basename='studio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('movie/', include('movie.urls')),
]