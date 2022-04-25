from django.contrib import admin
from ormapp.models import Actors

class ActorAdmin(admin.ModelAdmin):
    list_display = ["id","name","industoryname","noofmovies","hitmovies","screenname"]

admin.site.register(Actors,ActorAdmin)
