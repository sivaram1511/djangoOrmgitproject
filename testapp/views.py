from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def display_view(request):
    emp=Employee.objects.filter(ename__icontains='SU')
    return render(request,'testapp/index.html',{"employee":emp})
