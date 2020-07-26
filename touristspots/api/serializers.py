from rest_framework import serializers
from touristspots.api.models import TouristSpot, Favorite


"""
Serializers allow complex data such as querysets and model instances to be converted to native Python
datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide
deserialization, allowing parsed data to be converted back into complex types, after first validating the
incoming data.
"""


class TouristSpotSerializer(serializers.ModelSerializer):

    """
    TouristSpotViewSet - Will translate objects implemented in Model TouristSpot
    for viewing them in the DRF form.
    """
    class Meta:
        model = TouristSpot
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):

    """
    FavoriteViewSet - Will translate objects implemented in Model Favorite
    for viewing them in the DRF form.
    """

    class Meta:
        model = Favorite
        fields = '__all__'
