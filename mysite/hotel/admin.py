from django.contrib import admin
from .models import *


class HotelPhotoInLine(admin.TabularInline):
    model = HotelPhoto
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelPhotoInLine]


class RoomPhotoInLine(admin.TabularInline):
    model = RoomPhoto
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotoInLine]


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Booking)
admin.site.register(Rating)




