
from rest_framework import viewsets
from .models import Player, Match, Loot
from .serializers import PlayerSerializer, MatchSerializer, LootSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class LootViewSet(viewsets.ModelViewSet):
    queryset = Loot.objects.all()
    serializer_class = LootSerializer
