from django.contrib import admin
from .models import *


class HotelPhotoInLine(admin.TabularInline):
    model = HotelPhoto
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelPhotoInLine]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class RoomPhotoInLine(admin.TabularInline):
    model = RoomPhoto
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotoInLine]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Booking)
admin.site.register(Rating)
