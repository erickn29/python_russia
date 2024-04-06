from django.urls import path, include

from vacancies.views.default.vacancy.create import VacancyCreateView
from vacancies.views.default.vacancy.list import VacancyListV1View

vacancies_patterns = [
    path("", VacancyListV1View.as_view(), name="vacancies-list"),
    path("create/", VacancyCreateView.as_view(), name="vacancies-create"),
]

urlpatterns = [
    path("", include(vacancies_patterns)),
]
