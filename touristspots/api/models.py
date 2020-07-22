from django.db import models
from django.contrib.auth import get_user_model
# from django.contrib.gis.geos import Point

"""
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


class TouristSpot(models.Model):
    """
    This class contains the representation of the fields in the TouristSpot table.
    """
    # picture = models.ImageField(upload_to='pic_folder/', default='pic_folder/none/no-img.jpg')
    name = models.CharField(max_length=100)
    # geographical_location = models.PointField(geography=True, default=Point(0.0, 0.0))
    category = models.CharField(max_length=50)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)


class Favorite(models.Model):
    """
    This class contains the relationship between tourist spots and the tourist.
    Where a tourist spot may be a favorite of one or more tourists and a tourist
     may favor one or more tourist spots.
    """
    tourist = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tourist_spot = models.ForeignKey('TouristSpot', on_delete=models.CASCADE)

    favorided = models.DateTimeField('Favorided in', auto_now_add=True)
    unfavorited = models.DateTimeField('Unfavorited in', auto_now=True)
