from django.shortcuts import render
from onetomany.models import Department,Employee
# Create your views here.
def emp_dept_view(request):
    #emp=Employee.objects.all()
    #emp =Employee.objects.get(name='sidda')
    #department =Department.objects.all()
    #emp =Employee.objects.get(name='sidda').department
    emp =Employee.objects.filter(department__exact='Hr')
    return render(request,"deptwiseemployees.html",{"employee":emp})

