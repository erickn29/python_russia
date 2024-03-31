from django import template
from django.template.defaultfilters import register
from django.views.generic import ListView

from vacancies.models import Vacancy


class VacancyListV1View(ListView):
    model = Vacancy
    paginate_by = 20
    template_name = "vacancy/list.html"
    context_object_name = "objects_list"


@register.filter
def format_salary(value: float) -> str | float:
    value = int(value)
    if value and value > 999:
        return str(value // 1000) + ' ' + str(value)[len(str(value // 1000)):] + " руб."
    return value
