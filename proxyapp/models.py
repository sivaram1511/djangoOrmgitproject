from django.db import models

# Create your models here.
class Employee(models.Model):
    eno =models.IntegerField()
    ename =models.CharField(max_length=65)
    email =models.EmailField()
    esal =models.FloatField()
    eaddress =models.CharField(max_length=100)

class ProxyEmployee(Employee):
    class Meta:
        proxy =True
        ordering = ['-eno']


