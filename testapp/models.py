from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=65)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
# Create your models here.
