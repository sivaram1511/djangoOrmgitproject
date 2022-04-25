from django.shortcuts import render
from ormapp.models import Actors

def create_views(request):
    qs=Actors.objects.create(name="ntr",industoryname="tollywood",noofmovies=12,hitmovies=8,screenname="Jr NTR")
    qs.save
    print("succesfully created the record")
    if (qs!=0):
        qs=Actors.objects.all()
    return render(request,"actors.html",{"actors":qs})
def retrieve_view(request):
    qs =Actors.objects.all()

    return render(request,"actors.html",{"actors":qs})