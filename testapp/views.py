from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q,Avg
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    employee=Employee.objects.all().aggregate(Avg('esal'))

    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
    avgsal=Employee.objects.all().aggregate(Avg('esal'))
    return render(request,'testapp/index.html',{"avg":avgsal})