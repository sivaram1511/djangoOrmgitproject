from django.contrib import admin
from modelinheritenceapp import models
# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display =['name','email','address','rollno','marks']

admin.site.register(models.Student,Studentadmin)
class Teacheradmin(admin.ModelAdmin):
    list_display =["name",'email','address','subject','salary']
admin.site.register(models.Teacher,Teacheradmin)