from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(RoomPhoto)
admin.site.register(Booking)
admin.site.register(Rating)


