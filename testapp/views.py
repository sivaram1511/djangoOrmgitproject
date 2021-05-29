from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def display_view(request):
    emp=Employee.objects.filter(esal__gt=50000)

    return render(request,'testapp/index.html',{"employee":emp})
