from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators= [MinValueValidator(18), MaxValueValidator(65)],
                                           null=True, blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
        ('owner', 'owner'),
        ('client', 'client')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='client')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)
    city_name = models.CharField(max_length=32, unique=True, null=True, blank=True)
    hotel_address = models.CharField(max_length=32)
    country_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='country_user')
    country_image = models.ImageField(upload_to='country_image')

    def __str__(self):
        return f'{self.country_name}, {self.city_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_hotel')
    HOTEL_STARS = (
        ('3 stars', '3 stars'),
        ('4 stars', '4 stars'),
        ('5 stars', '5 stars')
    )
    hotel_stars = models.CharField(choices=HOTEL_STARS, max_length=12, default='3 stars')
    hotel_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel_name}, {self.user}, {self.country}'


    def get_avg_rating(self):
       totol = self.rating_hotel.all()
       if totol.exists():
           return round(sum([i.stars for i in totol]) /  totol.count(), 1)

       return 0

    def count_people(self):
        return self.rating_hotel.count()


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photos')
    hotel_image = models.ImageField(upload_to='hotel_image')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_room')
    room_number = models.PositiveSmallIntegerField(default=1)
    HOTEL_TYPES = (
        ('standard', 'standard'),
        ('suite', 'suite'),
        ('apartment', 'apartment')
    )
    hotel_types = models.CharField(choices=HOTEL_TYPES, max_length=12, default='standard')
    price = models.PositiveSmallIntegerField(default=0)
    HOTEL_STATUS = (
        ('free', 'free'),
        ('busy', 'busy'),
        ('reservation', 'reservation')
    )
    hotel_status = models.CharField(choices=HOTEL_STATUS, max_length=16, default='free')
    all_inclusive = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_number}, {self.hotel}'

class RoomPhoto(models.Model):
    room_image = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_list')
    image = models.ImageField(upload_to='room_image')


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='booking_hotel')
    booking_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    go_in = models.DateField()
    go_out = models.DateField()


    def __str__(self):
        return f'{self.user}'


class Rating(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rating_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rating_hotel')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range (1, 11)])
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    rating_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.text}'
