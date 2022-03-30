from django.db import models

# Create your models here.
class ContactInfo1(models.Model):
    name =models.CharField(max_length=64)
    email =models.EmailField()
    address =models.CharField(max_length=64)

class Student1(ContactInfo1):
    rollno =models.IntegerField()
    marks =models.IntegerField()


class Teacher1(ContactInfo1):
    subject =models.CharField(max_length=64)
    salary =models.FloatField()