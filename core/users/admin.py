from django.contrib import admin

from users.models import Employee, Employer


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass
