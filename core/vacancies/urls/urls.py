from django.urls import path, include

from vacancies.views.default.vacancy.list import VacancyListV1View

vacancies_patterns = [
    path('', VacancyListV1View.as_view(), name="vacancies-list")
]

urlpatterns = [
    path('', include(vacancies_patterns)),
]
