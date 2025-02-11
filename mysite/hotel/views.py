from rest_framework import viewsets
from .models import (UserProfile, Country, Hotel, Room, Booking, Rating)
from .serializers import (UserProfileSerializer, CountrySerializer, HotelSerializer, RoomSerializer,
                          BookingSerializer, RatingSerializer)
from django_filters .rest_framework import DjangoFilterBackend
from .filters import HotelFiler

from rest_framework .filters import SearchFilter, OrderingFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['hotel_name']
    ordering_fields = ['price']
    filterset_class = HotelFiler




class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


