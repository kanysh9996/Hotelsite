from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users',  UserProfileViewSet, basename='user_list')
router.register(r'country',  CountryViewSet, basename='country_list')
router.register(r'hotel',  HotelViewSet, basename='hotel_list')
router.register(r'room',  RoomViewSet, basename='room_list')
router.register(r'booking',  BookingViewSet, basename='booking_list')
router.register(r'rating',  RatingViewSet, basename='rating_list')


urlpatterns = [
    path('', include(router.urls)),

    ]