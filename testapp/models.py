from django.db import models
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('eno')
    def get_emp_sal_range(self,esal1,esal2):

        return super().get_queryset().filter(esal__range=(esal1,esal2)).order_by('esal')
    def get_emp_order_by(self,param):
        return super().get_queryset().order_by(param)
class  CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')
    def get_emp_sal_not_ename(self):
        return super().get_queryset().exclude(ename__startswith='b')

class Employee(models.Model):

    eno=models.IntegerField()
    ename=models.CharField(max_length=65)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)

    objects=CustomManager()
# Create your models here.
class ProxyEmployee(Employee):
    objects = CustomManager2()
    class Meta:
        proxy=True