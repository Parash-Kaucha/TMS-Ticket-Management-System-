from django.urls import path
from . import views

urlpatterns = [
    path('create_studio/', views.StudioVeiwSet.as_view({'get':'list', 'post':'create'}), name='studio'),
    path('create_movie/', views.MovieViewSet.as_view({'get':'list'}), name='create_movie'),
    path('get_details/', views.get_details),
    path('show_time/', views.ShowTimeViewSet.as_view({'get':'list', 'post':'create'}), name='show_time'),
    path('show_time/<int:id>/', views.ShowTimeViewSet.as_view({'put':'update', 'delete':'destroy', 'get':'retrieve'}), name='show_time')
]