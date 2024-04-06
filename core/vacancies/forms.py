from betterforms.forms import BetterModelForm
from betterforms.multiform import MultiModelForm
from django import forms
from django.db import IntegrityError
from django.forms import BooleanField

from users.models import Employer
from vacancies.models import Vacancy, StackTool, Company


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-control  mb-4"


class StackForm(BaseModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "sql,html,power bi"}),
        label="Ключевые навыки (через запятую):",
        required=False,
    )

    class Meta:
        model = StackTool
        exclude = ['created_at', ]


class VacancyForm(BaseModelForm):
    class Meta:
        model = Vacancy
        exclude = (
            "company",
            "stack",
            "grade",
            "created_at",
            "link",
        )


class CreateVacancyMultiForm(MultiModelForm):
    form_classes = {
        'vacancy': VacancyForm,
        'stack': StackForm,
    }

    def save(self, commit=True):
        objects = super(CreateVacancyMultiForm, self).save(commit=False)

        if commit:
            stack_name_list = objects["stack"].name.split(",") if objects[
                "stack"].name else []
            stack_obj_list = []
            for stack in stack_name_list:
                obj, _ = StackTool.objects.get_or_create(
                    name=stack.strip().replace(" ", "_").lower(),
                )
                stack_obj_list.append(obj)
            employer = Employer.objects.filter(user_id=self.data["user_id"]).first()
            if not employer:
                return objects
            vacancy = objects["vacancy"]
            vacancy.company = employer.company
            try:
                vacancy.save()
                vacancy.stack.set(stack_obj_list)
            except IntegrityError:
                return objects

        return objects
