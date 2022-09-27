from django.urls import path, include
from .views.views import EvangelionViewsSet, CharactersViewSet, UnitsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("evangelion", EvangelionViewsSet, basename="evangelion")
router.register("character", CharactersViewSet, basename="character")
router.register("unit", UnitsViewSet, basename="unit")

urlpatterns = [
    path('', include(router.urls))
]