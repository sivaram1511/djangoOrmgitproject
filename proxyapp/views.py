from django.shortcuts import render
from proxyapp.models import Employee,ProxyEmployee
# Create your views here.
def emp_views(request):
    emp =Employee.objects.all()
    proxyemp =ProxyEmployee.objects.all()
    return render(request,'index.html',{"employee":emp,"proxy":proxyemp})