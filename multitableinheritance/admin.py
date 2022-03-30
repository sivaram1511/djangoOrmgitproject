from django.contrib import admin
from multitableinheritance.models import ContactInfo1,Student1,Teacher1
# Register your models here.
class ContactInfoAdmin1(admin.ModelAdmin):
    list_display =["id","name",'email',"address"]

class StudentAdmin1(admin.ModelAdmin):
    list_display=['id','rollno','marks']

class TeacherAdmin1(admin.ModelAdmin):
    list_display=['id','subject','salary']

admin.site.register(ContactInfo1,ContactInfoAdmin1)
admin.site.register(Student1,StudentAdmin1)
admin.site.register(Teacher1,TeacherAdmin1)