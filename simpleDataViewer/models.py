import pandas
from django.db import models

# Create your models here.
class EmoArgument(models.Model):
    argument = models.TextField()
    arg_strength = models.FloatField()
    stance = models.IntegerField()
    topic = models.TextField()
    label = models.PositiveIntegerField()


#class FavoriteArguments(models.Model):
 #   favargument = models.TextField()
