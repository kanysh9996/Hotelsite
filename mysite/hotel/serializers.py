from rest_framework import serializers
from . models import ( UserProfile, Country, Hotel, Room,  Booking, Rating, RoomPhoto)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name', 'id']


class CountryHotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_name', ]


class RoomPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomPhoto
        fields = ['image']

class HotelPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['hotel_image']

class HotelWideSerializer(serializers.ModelSerializer):
    user = UsersProfileSerializer()
    country = CountryHotelSerializer()
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['hotel_name','user', 'country', 'hotel_stars', 'hotel_description',
                  'date', 'price', 'hotel_photos', 'get_avg_rating']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'hotel_stars']


class CountryWideSerializer(serializers.ModelSerializer):
    country_hotel =HotelWideSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'city_name', 'hotel_address', 'country_image', 'country_hotel']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','hotel_types']

class RoomsSerializer(serializers.ModelSerializer):
    room_list = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['hotel', 'room_number', 'hotel_types', 'room_list']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
