from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee
from django.db.models import Q,Avg,Min,Max,Sum
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all()
    '''employee=ProxyEmployee.objects.values('ename',ename__contains='sa')
    return render(request,'testapp/index.html',{"employee":employee})'''
    #employee=Employee.objects.
    e=Employee()
    e.eno=127
    e.ename='kagithala'
    e.esal=90890
    e.eaddr="Tuni"
    employee=Employee.objects.create(e)
    for i in employee:
        print(i)
    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
   sumofesal=Employee.objects.count()
   return render(request,'testapp/index.html',{"sumsal":sumofesal})