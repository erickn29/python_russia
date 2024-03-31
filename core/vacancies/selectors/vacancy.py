from django.db.models import QuerySet

import django_filters
from django.forms import BooleanField

from vacancies.models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    class Meta:
        model = Vacancy
        exclude = (
            "created_at",
            "title",
            "text",
            "stack",
            "link",
            "salary_to",
            "company",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.form.fields.items():
            field.widget.attrs["class"] = "form-control mb-4"


def vacancy_queryset(filters) -> QuerySet[Vacancy]:
    return VacancyFilter(filters).qs
