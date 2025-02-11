from django_filters import FilterSet
from .models import Hotel

class HotelFiler(FilterSet):
    class Meta:
        model = Hotel
        fields ={
            'country': ['exact'],
            'date': ['exact'],
        }
