from django.urls import reverse_lazy
from django.views.generic import CreateView

from vacancies.forms import CreateVacancyMultiForm
from vacancies.models import Vacancy


class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = CreateVacancyMultiForm
    template_name = "vacancy/create.html"
    success_url = reverse_lazy("vacancies-list")
