# from touristspots.api.permissions import IsAuthenticatedUserOwner
from allauth.socialaccount.providers.facebook.views import \
    FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import filters, viewsets


from touristspots.api.models import Favorite, TouristSpot, Picture
from touristspots.api.serializers import (FavoriteSerializer,
                                          TouristSpotSerializer, PictureSerializer)


class PictureViewSet(viewsets.ModelViewSet):

    serializer_class = PictureSerializer

    def get_queryset(self):
        """
        This view should return a list of all the picture
        tourist spots for the currently authenticated user.
        """
        user = self.request.user
        return Picture.objects.filter(user=user)


class TouristSpotViewSet(viewsets.ModelViewSet):

    """
    TouristSpotViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = TouristSpot.objects.all()
    serializer_class = TouristSpotSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

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

    serializer_class = FavoriteSerializer

    def get_queryset(self):
        """
        This view should return a list of all the favorite
        tourist spots for the currently authenticated user.
        """
        user = self.request.user
        return Favorite.objects.filter(user=user)


class FacebookLogin(SocialLoginView):
    """
    Visualization for access with Facebook
    """
    adapter_class = FacebookOAuth2Adapter
