from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q,Avg,Min
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    employee=Employee.objects.all().order_by('esal')[0:1]

    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
   minsal=Employee.objects.all().aggregate(Min('esal'))
   return render(request,'testapp/index.html',{"minsal":minsal})