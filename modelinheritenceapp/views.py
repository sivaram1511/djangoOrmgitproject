from django.shortcuts import render
from modelinheritenceapp.models import Student
# Create your views here.
def student_view(request):
    qs =Student.objects.all()
    print(type(qs))

    return render(request,"index.html",{'stu':qs})
print("succesfully")
