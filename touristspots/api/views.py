from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from touristspots.api.models import Favorite, TouristSpot
from touristspots.api.serializers import TouristSpotSerializer, FavoriteSerializer

from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point


class TouristSpotViewSet(viewsets.ModelViewSet):

    """
    TouristSpotViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['name', 'category']

    lat = 52.5
    lng = 1.0
    radius = 5
    point = Point(lng, lat)
    clients_within_radius = queryset.filter(
        geographical_location__distance_lt=(
            point, Distance(km=radius)
        )
    )


class FavoriteViewSet(viewsets.ModelViewSet):

    """
    FavoriteViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)
