from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from touristspots.api.models import Favorite, TouristSpot
from touristspots.api.serializers import TouristSpotSerializer, FavoriteSerializer


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
