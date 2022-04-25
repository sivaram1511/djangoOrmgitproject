from django.db import models

# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=100)
    industoryname = models.CharField(max_length=125)
    noofmovies = models.IntegerField()
    hitmovies = models.IntegerField()
    screenname = models.CharField(max_length=100)