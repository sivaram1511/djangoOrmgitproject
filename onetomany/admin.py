from django.contrib import admin
from onetomany.models import Department,Employee
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['id','name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =["id","name","age","department"]

# admin.site.register(Department,DepartmentAdmin)
# admin.site.register(Employee,EmployeeAdmin)
