from django.db import models
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')
class Employee(models.Model):

    eno=models.IntegerField()
    ename=models.CharField(max_length=65)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)

    objects=CustomManager()
# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    marks=models.IntegerField(3)