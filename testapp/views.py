from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
# Create your views here.
def display_view(request):
    #emp=Employee.objects.filter(eno__in=[45,48,55,34,90,100,67,18])
    #emp=Employee.objects.filter(ename__startswith='s')
    #emp=Employee.objects.filter(eaddr__exact='delhi')
    #emp=Employee.objects.filter(ename__startswith='b',eno__range=(30,80))
    #emp=Employee.objects.filter(ename__contains='iy')&Employee.objects.filter(esal__gt=20000)
    employee=Employee.objects.all().order_by('ename')#[0:5]
    return render(request,'testapp/index.html',{"employee":employee})
