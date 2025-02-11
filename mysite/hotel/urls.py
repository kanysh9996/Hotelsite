from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'booking',  BookingViewSet, basename='booking_list')


urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelAPIView.as_view(), name='hotel_list' ),
    path('hotel/<int:pk>/', HotelWideAPIView.as_view(), name='hotel_wide'),
    path('country/', CountryAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/',  CountryWideAPIView.as_view(), name='country_wide'),
    path('commit/', RatingAPIView.as_view(), name='rating'),
    path('room/', RoomAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomSAPIView.as_view(), name='room_wide'),
    path('user/', UserProfileAPIView.as_view(), name='user_lisr'),
    path('user/<int:pk>/', UsersProfileAPIView.as_view(), name='user_create')

    ]