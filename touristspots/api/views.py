from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from touristspots.api.models import TouristSpot
from touristspots.api.serializers import TouristSpotSerializer


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
