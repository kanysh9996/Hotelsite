from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_list')
router.register(r'hotel_create', HotelCreateViewSet, basename='hotel_create')
router.register(r'booking',BookingViewSet, basename='booking' )


urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list' ),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_wide'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/',  CountryDetailAPIView.as_view(), name='country_detail'),
    path('room/', RoomAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomSAPIView.as_view(), name='room_wide'),
    path('rating/', RatingListAPIView.as_view(), name='rating_list'),
    path('rating/<int:pk>/', RatingDetailAPIView.as_view(), name='rating_detail'),


]