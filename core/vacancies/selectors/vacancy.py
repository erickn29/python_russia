from django.db.models import QuerySet, Q

import django_filters
from django.forms import BooleanField, FloatField
from django.http import QueryDict

from vacancies.models import Vacancy


class VacancyFilter(django_filters.FilterSet):
    class Meta:
        model = Vacancy
        exclude = (
            "created_at",
            "title",
            "text",
            "grade",
            "stack",
            "link",
            "salary_to",
        )

    company = django_filters.CharFilter(
        field_name="company__name",
        lookup_expr="icontains",
        label="Компания",
    )
    salary_from = django_filters.NumberFilter(
        # field_name="salary_from",
        method="salary_filter",
        label="Зарплата от",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.form.fields.items():
            field.widget.attrs["class"] = "form-control mb-4"
            if name == "salary_from":
                field.widget.attrs["value"] = 30000

    def salary_filter(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(salary_from__gte=int(value)) |
                Q(salary_from=None, salary_to__gte=value))
        return queryset


def vacancy_queryset(filters) -> QuerySet[Vacancy]:
    return VacancyFilter(filters).qs


# class StudentFilterSet(rest_filters.FilterSet):
#     fullname = rest_filters.CharFilter(
#         method="fullname_filter", label="active_contract"
#     )
#     school_came_from_is_empty = rest_filters.BooleanFilter(
#         field_name="school_came_from", lookup_expr="isnull"
#     )
#     school_going_to_is_empty = rest_filters.BooleanFilter(
#         field_name="school_going_to", lookup_expr="isnull"
#     )
#
#     def fullname_filter(self, queryset, name, value):
#         if value:
#             return queryset.filter(search_fullname(fullname=value))
#         return queryset
#
#     class Meta:
#         model = Student
#         fields = [
#             "first_name",
#             "last_name",
#             "fullname",
#             "patronymic",
#             "grade",
#             "education_cost",
#             "school",
#             "school_came_from_is_empty",
#             "school_going_to_is_empty",
#             "lms_id",
#         ]
