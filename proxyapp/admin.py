from django.contrib import admin
from proxyapp.models import Employee,ProxyEmployee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =["eno","ename","email","esal","eaddress"]
@admin.register(ProxyEmployee)
class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display =["eno","ename","email","esal","eaddress"]
