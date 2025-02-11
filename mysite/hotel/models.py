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

    def str(self):
        return f'{self.first_name}, {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)
    city_name = models.CharField(max_length=32, unique=True, null=True, blank=True)
    hotel_address = models.CharField(max_length=32)
    country_image = models.ImageField(upload_to='country_image')

    def str(self):
        return f'{self.country_name}, {self.city_name}'


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    HOTEL_STARS = (
        ('3 stars', '3 stars'),
        ('4 stars', '4 stars'),
        ('5 stars', '5 stars')
    )
    hotel_stars = models.CharField(choices=HOTEL_STARS, max_length=12, default='3 stars')
    hotel_description = models.TextField()
    date = models.DateField()
    price = models.PositiveSmallIntegerField(default=0)

    def str(self):
        return f'{self.hotel_name}, {self.user}, {self.country}'


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_image')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField(default=1)
    HOTEL_TYPES = (
        ('standard', 'standard'),
        ('suite', 'suite'),
        ('apartment', 'apartment')
    )
    hotel_types = models.CharField(choices=HOTEL_TYPES, max_length=12, default='standard')

    def str(self):
        return self.hotel

class RoomPhoto(models.Model):
    room_image = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_image')


class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    booking_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    booking_room = models.ForeignKey(Room, on_delete=models.CASCADE)

    HOTEL_STATUS = (
        ('free', 'free'),
        ('busy', 'busy'),
        ('reservation', 'reservation')
    )
    hotel_status = models.CharField(choices=HOTEL_STATUS, max_length=16, default='free')
    check_unique = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='check_unique')
    cancel_booking = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='cancel_booking')

    def str(self):
        return f'{self.user}'


class Rating(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rating_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range (1, 6)])
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    rating_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user}, {self.text}'
