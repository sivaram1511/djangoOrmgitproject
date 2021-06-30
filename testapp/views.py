from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee
from django.db.models import Q,Avg,Min,Max,Sum
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    #employee=Employee.objects.all().aggregate(Avg('esal'))
    #employee=Employee.objects.all().order_by('-esal')[:1]
    #employee=Employee.objects.order_by('-esal')[:2]
    #employee=Employee.objects.all().filter(esal__lt=25000)
    #q1=Employee.objects.all().aggregate(Avg('esal'))
    employee=Employee.objects.exclude(id__range=[0,10])



    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
   sumofesal=Employee.objects.count()
   return render(request,'testapp/index.html',{"sumsal":sumofesal})