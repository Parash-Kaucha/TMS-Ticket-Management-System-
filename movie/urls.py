from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'studio', views.StudioVeiwSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'showtime', views.ShowTimeViewSet)
router.register(r'ticket', views.TicketBookingViewSet)
urlpatterns = router.urls