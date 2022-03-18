from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee
from django.db.models import Q,Avg,Min,Max,Sum,F,Count
from django.db.models.functions import Lower
# Create your views here.
def display_view(request):
    #qs=Employee.objects.filter(~Q(eno__lt=100))
    #qs=Employee.objects.all().aggregate(Max('esal'))
    #qs=Employee.objects.exclude(esal=99870).order_by("-esal")
    #a=set()
    #qs=Employee.objects.order_by('-esal')
    #for i in qs:
       # a.add(i.esal)
    #c=sorted(a)
    #print(c)
    #xy=Employee.objects.filter(esal=c[-2])
    #qs=[qs1,]
    qs1 =Employee.objects.filter(ename__istartswith ="h")

    #qs1 =Employee.objects.all()
    #print(type(qs1))
    return render(request,'testapp/index.html',{'employee':qs1})
def aggregate_view(request):
   qs=Employee.objects.all().exclude(esal=5000)
   return render(request,'testapp/index.html',{"maxsal":qs})