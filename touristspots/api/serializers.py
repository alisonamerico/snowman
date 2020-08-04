from rest_framework import serializers
from touristspots.api.models import Favorite, Picture, TouristSpot


"""
Serializers allow complex data such as querysets and model instances to be converted to native Python
datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide
deserialization, allowing parsed data to be converted back into complex types, after first validating the
incoming data.
"""


class PictureSerializer(serializers.ModelSerializer):

    """
    PictureSerializer - It will be defined which fields
    will be displayed in the Picture view.
    """

    user = serializers.ReadOnlyField(source='user.first_name')
    tourist_spot = serializers.ReadOnlyField(source='tourist_spot.name')

    class Meta:
        model = Picture
        fields = ('id', 'picture', 'tourist_spot', 'user')


class TouristSpotSerializer(serializers.ModelSerializer):

    """
    TouristSpotSerializer - It will be defined which fields
    will be displayed in the TouristSpot view.
    """
    pictures = PictureSerializer(source='picture_set', many=True, read_only=True)

    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'geographical_location', 'category', 'pictures', 'created', 'modified',)

    def create(self, validated_data):
        pictures_data = self.context.get('view').request.FILES
        tourist_spot = TouristSpot.objects.create(**validated_data)
        for picture_data in pictures_data.values():
            Picture.objects.create(tourist_spot=tourist_spot, picture=picture_data)
        return tourist_spot


class FavoriteSerializer(serializers.ModelSerializer):

    """
    FavoriteSerializer - It will be defined which fields
    will be displayed in the Favorite view.
    """
    user = serializers.ReadOnlyField(source='user.first_name')
    tourist_spot = serializers.ReadOnlyField(source='tourist_spot.name')

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'tourist_spot',)
