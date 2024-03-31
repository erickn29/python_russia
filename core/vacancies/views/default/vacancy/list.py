from django import template
from django.template.defaultfilters import register
from django.views.generic import ListView

from vacancies.models import Vacancy
from vacancies.selectors.vacancy import vacancy_queryset, VacancyFilter


class VacancyListV1View(ListView):
    model = Vacancy
    paginate_by = 10
    template_name = "vacancy/list.html"
    context_object_name = "objects_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = "vacancies-list"
        context["form"] = VacancyFilter().form
        context["count"] = self.get_queryset().count()
        return context

    def get_queryset(self):
        return vacancy_queryset(self.request.GET)

    # def get(self, request, *args, **kwargs):
    #     pass


@register.filter
def format_salary(value: float) -> str | float:
    value = int(value)
    if value and value > 999:
        return str(value // 1000) + ' ' + str(value)[len(str(value // 1000)):] + " руб."
    return value
