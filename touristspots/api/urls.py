from rest_framework import routers
from touristspots.api.views import TouristSpotViewSet, FavoriteViewSet

"""
Registration of urls available in the application
"""

router = routers.DefaultRouter(trailing_slash=True)

router.register('touristspots', TouristSpotViewSet)
router.register('favorites', FavoriteViewSet)

urlpatterns = router.urls
