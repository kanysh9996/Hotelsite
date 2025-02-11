from .models import Rating, Hotel, Country
from modeltranslation.translator import TranslationOptions,register

@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('text', )


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_description', )

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name', 'city_name', 'hotel_address' )
