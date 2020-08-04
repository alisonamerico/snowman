from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from touristspots.api.models import Picture, TouristSpot, Favorite

"""
list_display - Fields to be viewed in django admin
search_fields - Fields that will be viewed for django admin search
list_filter - Fields to be filtered
"""


@admin.register(Picture)
class PictureAdmin(OSMGeoAdmin):
    """
    It will be defined which fields will be displayed
    in the Picture view in the Admin
    """
    list_display = ('picture', 'tourist_spot', 'user',)
    search_fields = ['picture', 'tourist_spot', 'user']
    ordering = ('-tourist_spot',)


@admin.register(TouristSpot)
class TouristSpotAdmin(OSMGeoAdmin):
    """
    It will be defined which fields will be displayed
    in the TouristSpot view in the Admin
    """
    list_display = ('name', 'geographical_location', 'pictures', 'category', 'created', 'modified')
    search_fields = ['pictures', 'name', 'category']
    ordering = ('-created',)


@admin.register(Favorite)
class FavoriteAdmin(OSMGeoAdmin):
    """
    It will be defined which fields will be displayed
    in the Favorite view in the Admin
    """
    list_display = ('user', 'tourist_spot')
    search_fields = ['user', 'tourist_spot']
    ordering = ('-tourist_spot',)
