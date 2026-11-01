
from rest_framework.routers import DefaultRouter
from .views import DogViewSet, BreedViewSet

# Create a router for our API
router = DefaultRouter()

# Connect dogs endpoint to DogViewSet
router.register(r'dogs', DogViewSet, basename='dog')

# Connect breeds endpoint to BreedViewSet
router.register(r'breeds', BreedViewSet, basename='breed')

# Store all URLs created by the router
urlpatterns = router.urls
