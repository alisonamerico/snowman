from rest_framework import routers
from touristspots.api.views import TouristSpotViewSet, FavoriteViewSet, PictureViewSet

"""
Registration of urls available in the application
"""
app_name = 'api'
router = routers.DefaultRouter(trailing_slash=True)

router.register('touristspots', TouristSpotViewSet, basename='touristspots')
router.register('favorites', FavoriteViewSet, basename='favorites')
router.register('pictures', PictureViewSet, basename='pictures')

urlpatterns = router.urls
