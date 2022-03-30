from django.shortcuts import render
from multitableinheritance.models import ContactInfo1,Student1
def studenet_view(request):
    contactinfo1 =ContactInfo1.objects.all()
    studentinfo1 =Student1.objects.all()
    return render(request,"index.html",{"contact":contactinfo1,"student":studentinfo1})
# Create your views here.
