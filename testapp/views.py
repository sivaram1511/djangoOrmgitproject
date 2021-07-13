from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee
from django.db.models import Q,Avg,Min,Max,Sum,F
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    #qs=Employee.objects.filter(~Q(eno__lt=100))
    qs=Employee.objects.filter(ename__startswith='r').values('ename','esal')

    print(qs.query)



    return render(request,'testapp/index.html',{'employee':qs})
def aggregate_view(request):
   sumofesal=Employee.objects.count()
   return render(request,'testapp/index.html',{"sumsal":sumofesal})