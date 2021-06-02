from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q,Avg,Min,Max
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    employee=Employee.objects.all().order_by('-eno')[1:2]

    return render(request,'testapp/index.html',{"employee":employee})
def aggregate_view(request):
   maxeno=Employee.objects.all().aggregate(Max('eno'))
   return render(request,'testapp/index.html',{"minsal":maxeno})