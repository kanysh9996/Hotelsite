from rest_framework import serializers
from . models import ( UserProfile, Country, Hotel, HotelPhoto, Room,  Booking, Rating, RoomPhoto)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")


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


class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', '']


class HotelDetailSerializer(serializers.ModelSerializer):
    user = UserSimpleProfileSerializer()
    country = CountryHotelSerializer()
    hotel_photos = HotelPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    hotel_room = RoomSimpleSerializer(many=True, read_only=True)
    rating_hotel = RatingSerializer(many=True,read_only=True)
    date = serializers.DateTimeField(format('%d-%m-%Y'))
    count_people =serializers.ModelSerializer()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'hotel_stars', 'hotel_description',
                  'date', 'hotel_photos', 'user', 'get_avg_rating', 'hotel_room', 'rating_hotel', 'count_people']


    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def count_people(self,obj):
        return obj.count_people()


class RatingDetailSerializer(serializers.ModelSerializer):
    rating_hotel = HotelListSerializer()
    class Meta:
        model = Rating
        fields = ['user', 'stars', 'parent', 'text', 'rating_date', 'rating_hotel']


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
    user = UserSimpleProfileSerializer()
    class Meta:
        model = Booking
        fields = ['user', 'booking_hotel', 'booking_room', 'go_in', 'go_out']


