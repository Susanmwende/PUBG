# game/urls.py

from django.urls import path
from .views import PlayerViewSet, MatchViewSet, LootViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'loot', LootViewSet)

urlpatterns = router.urls