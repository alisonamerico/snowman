from rest_framework import routers
from touristspots.api.views import TouristSpotViewSet

"""
Registration of urls available in the application
"""

router = routers.DefaultRouter(trailing_slash=True)

router.register('touristspots', TouristSpotViewSet)


urlpatterns = router.urls
