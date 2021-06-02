from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q,Avg,Min,Max,Sum
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    employee=Employee.objects.filter(esal__gt=15000)[0:5]

    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
   sumofesal=Employee.objects.count()
   return render(request,'testapp/index.html',{"sumsal":sumofesal})