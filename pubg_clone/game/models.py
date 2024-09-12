
from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)

class Match(models.Model):
    players = models.ManyToManyField(Player)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

class Loot(models.Model):
    name = models.CharField(max_length=100)
    position_x = models.FloatField()
    position_y = models.FloatField()
# Create your models here.
