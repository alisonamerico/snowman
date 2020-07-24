from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from touristspots.api.models import TouristSpot, Favorite

"""
list_display - Fields to be viewed in django admin
search_fields - Fields that will be viewed for django admin search
list_filter - Fields to be filtered
"""


@admin.register(TouristSpot)
class TouristSpotAdmin(OSMGeoAdmin):

    list_display = ('name', 'picture', 'geographical_location', 'category', 'created', 'modified')
    search_fields = ['picture', 'name', 'category']
    ordering = ('-created',)


@admin.register(Favorite)
class FavoriteAdmin(OSMGeoAdmin):

    list_display = ('tourist', 'tourist_spot')
    search_fields = ['tourist', 'tourist_spot']
    ordering = ('-tourist_spot',)
