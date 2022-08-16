from django.db import models

# Create your models here.

class EmoArguments(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    argument = models.TextField()
    arg_strength = models.FloatField()
    topic = models.TextField()
    stance = models.PositiveIntegerField()
    label = models.PositiveIntegerField()

