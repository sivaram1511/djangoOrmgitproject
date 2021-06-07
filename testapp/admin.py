from django.contrib import admin
from testapp.models import Employee,ProxyEmployee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']
class ProxyEmployeeadmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(ProxyEmployee,ProxyEmployeeadmin)

