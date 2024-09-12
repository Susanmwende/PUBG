# game/serializers.py

from rest_framework import serializers
from .models import Player, Match, Loot

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class LootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loot
        fields = '__all__'