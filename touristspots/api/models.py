# from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

"""
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


class Picture(models.Model):
    """
    This class contains the representation of the fields in the Picture table.
    """
    picture = models.ImageField(upload_to='pic_folder/')
    tourist_spot = models.ForeignKey('TouristSpot', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'

    def __str__(self):
        """A string representation of the model."""
        return f'{self.picture}, {self.tourist_spot.name}, {self.user}'


class TouristSpot(models.Model):
    """
    This class contains the representation of the fields in the TouristSpot table.
    """
    CATEGORY_CHOICES = [
        ('PARK', 'Park'),
        ('MUSEUM', 'Museum'),
        ('THEATER', 'Theater'),
        ('MONUMENT', 'Monument'),
    ]

    pictures = models.ForeignKey('api.Picture', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    geographical_location = models.PointField(geography=True, default=Point(0.0, 0.0))
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'TouristSpot'
        verbose_name_plural = 'TouristSpots'
        ordering = ['-created']

    def __str__(self):
        """A string representation of the model."""
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super(TouristSpot, self).save(*args, **kwargs)


class Favorite(models.Model):
    """
    This class contains the relationship between tourist spots and the tourist.
    Where a tourist spot may be a favorite of one or more tourists and a tourist
     may favor one or more tourist spots.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tourist_spot = models.ForeignKey('TouristSpot', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        ordering = ['-tourist_spot']

    def __str__(self):
        """A string representation of the model."""
        return f'{self.tourist_spot}, {self.user}'
