from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee
from django.db.models import Q,Avg,Min,Max,Sum
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all()
    '''employee=ProxyEmployee.objects.values('ename',ename__contains='sa')
    return render(request,'testapp/index.html',{"employee":employee})'''
    emp=Employee.objects.values_list("eno",flat=True).order_by('eno')
    return render(request,'testapp/index.html',{"emp":emp})
def aggregate_view(request):
   sumofesal=Employee.objects.count()
   return render(request,'testapp/index.html',{"sumsal":sumofesal})