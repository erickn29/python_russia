from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    class Sex(models.TextChoices):
        MALE = "M", "Мужчина"
        FEMALE = "F", "Женщина"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    given = models.CharField(max_length=32, verbose_name="Имя")
    family = models.CharField(max_length=32, verbose_name="Фамилия")
    patronymic = models.CharField(
        max_length=32,
        verbose_name="Отчество",
        null=True,
        blank=True,
    )
    birthday = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    sex = models.CharField(
        max_length=16,
        verbose_name="Пол",
        null=True,
        blank=True,
        choices=Sex.choices,
    )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        ordering = ("family",)

    def __str__(self):
        return f"{self.family} {self.given} {self.patronymic} {self.birthday}"


class Employer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(
        "vacancies.Company",
        on_delete=models.DO_NOTHING,
        verbose_name="Компания",
        related_name="employers",
    )
    given = models.CharField(max_length=32, verbose_name="Имя")
    family = models.CharField(max_length=32, verbose_name="Фамилия")
    patronymic = models.CharField(
        max_length=32,
        verbose_name="Отчество",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Работодатели"
        ordering = ("company", "family")
        unique_together = ("company", "family", "given")

    def __str__(self):
        return f"{self.company}: {self.family} {self.given}"
