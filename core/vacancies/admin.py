from django.contrib import admin

from vacancies.models import StackTool, City, Company, Vacancy, Resume, JobPlace


@admin.register(StackTool)
class StackToolAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    pass


@admin.register(JobPlace)
class JobPlaceAdmin(admin.ModelAdmin):
    pass
