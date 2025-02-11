from rest_framework import viewsets, generics
from .models import (UserProfile, Country, Hotel, Room, Booking, Rating)
from .serializers import (UserProfileSerializer,  CountryListSerializer,  CountryDetailSerializer, HotelCreateSerializer,
                          HotelListSerializer, HotelDetailSerializer, RoomSerializer, RoomsSerializer,
                          BookingSerializer, RatingListSerializer, RatingDetailSerializer)
from django_filters .rest_framework import DjangoFilterBackend
from .filters import HotelFiler
from rest_framework .filters import SearchFilter, OrderingFilter
from .permissions import CheckStatus, CheckRatings, CheckBooking


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer


class CountryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class HotelCreateViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer
    permission_classes = [CheckStatus]



class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['hotel_name']
    ordering_fields = ['price']
    filterset_class = HotelFiler


class HotelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomSAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomsSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckBooking]


class RatingListAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingListSerializer
    permission_classes = [CheckRatings]


class RatingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingDetailSerializer



