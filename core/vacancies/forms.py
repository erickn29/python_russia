from django import forms
from django.forms import BooleanField

from vacancies.models import Vacancy


class VacancyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            if not isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-control"

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
