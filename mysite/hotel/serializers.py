from rest_framework import serializers
from . models import ( UserProfile, Country, Hotel, HotelPhoto, Room,  Booking, Rating, RoomPhoto)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSimpleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class UserProProfileSerializer(serializers.ModelSerializer):
    country_user = UserProfileSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ['first_name', 'country_user']


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'city_name', 'country_image']


class CountryHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['city_name', 'country_name' ]



class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ['image']


class HotelPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['hotel_image']


class RoomSimpleSerializer(serializers.ModelSerializer):
    room_image = RoomPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'hotel_types', 'price', 'hotel_status', 'room_image']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProProfileSerializer()
    rating_date = serializers.DateTimeField(format('%d-%m-%Y'))

    class Meta:
        model = Rating
        fields = ['id', 'user', 'stars', 'parent', 'text', 'rating_date']

class RatingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'rating_hotel', 'stars', 'parent', 'text', 'rating_date']


class RatingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'user', 'country', 'hotel_stars', 'hotel_description', 'date']



class HotelListSerializer(serializers.ModelSerializer):
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)
    country = CountryHotelSerializer()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'country', 'hotel_photos', 'hotel_description']



class HotelDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleProfileSerializer()
    country = CountryHotelSerializer()
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    hotel_room = RoomSimpleSerializer(many=True, read_only=True)
    rating_hotel = RatingSerializer(many=True)
    date = serializers.DateTimeField(format('%d-%m-%Y'))

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'hotel_stars', 'hotel_description',
                  'date', 'hotel_photos', 'user', 'get_avg_rating', 'hotel_room', 'rating_hotel']


    def get_avg_rating(self,obj):
        return obj.get_avg_rating()


class CountryDetailSerializer(serializers.ModelSerializer):
    country_hotel = HotelListSerializer(many=True, read_only=True)

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


