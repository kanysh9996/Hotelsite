from rest_framework import viewsets, generics
from .models import (UserProfile, Country, Hotel, Room, Booking, Rating)
from .serializers import (UserProfileSerializer, CountrySerializer,  CountryWideSerializer,
                          HotelSerializer, HotelWideSerializer, RoomSerializer, RoomsSerializer,
                          BookingSerializer, RatingSerializer)
from django_filters .rest_framework import DjangoFilterBackend
from .filters import HotelFiler
from rest_framework .filters import SearchFilter, OrderingFilter

class UserProfileAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UsersProfileAPIView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CountryAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryWideAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryWideSerializer


class HotelAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['hotel_name']
    ordering_fields = ['price']
    filterset_class = HotelFiler


<<<<<<< HEAD
class RoomViewSet(viewsets.ModelViewSet):
=======
class HotelWideAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelWideSerializer


class RoomAPIView(generics.ListAPIView):
>>>>>>> 2e9562ba21e163f486c94f55caa765845d42219b
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomSAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RatingAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


