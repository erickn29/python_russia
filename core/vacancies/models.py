from django.db import models


class Language(models.TextChoices):
    PYTHON = "python", "Python"
    PHP = "php", "PHP"
    JAVASCRIPT = "javascript", "JavaScript"
    C_PP = "cpp", "C++"
    C_SHARP = "csharp", "C#"
    JAVA = "java", "Java"
    GOLANG = "golang", "Go"
    RUST = "rust", "Rust"
    RUBY = "ruby", "Ruby"
    SQL = "sql", "SQL"


class Speciality(models.TextChoices):
    DEVOPS = "DevOps-инженер"
    ANALYTICS = "Аналитик"
    DATA_SCIENTIST = "Дата-сайентист"
    MENTOR = "Преподаватель"
    DEVELOPER = "Программист"
    LEAD = "Руководитель группы разработки"
    SYSTEM_ADMINISTRATOR = "Системный администратор"
    QA = "Тестировщик"


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class StackTool(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Стек"
        ordering = ("name",)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=32, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Company(BaseModel):
    city = models.ForeignKey(
        "vacancies.City",
        verbose_name="Город",
        on_delete=models.DO_NOTHING,
        related_name="companies",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ("name",)
        unique_together = ("city", "name")

    def __str__(self):
        return self.name


class Vacancy(BaseModel):
    class Experience(models.TextChoices):
        NO_EXPERIENCE = "no_experience", "Без опыта"
        BETWEEN_1_3 = "between_1_2", "От 1 до 3 лет"
        BETWEEN_3_5 = "between_3_5", "От 3 до 5 лет"
        MORE_THAN_5 = "more_than_5", "Более 5 лет"

    class Grade(models.TextChoices):
        TRAINEE = "trainee", "Стажер"
        JUNIOR = "junior", "Джуниор"
        MIDDLE = "middle", "Миддл"
        SENIOR = "senior", "Сеньор"
        LEAD = "lead", "Лид"

    company = models.ForeignKey(
        "vacancies.Company",
        verbose_name="Компания",
        on_delete=models.CASCADE,
        related_name="vacancies",
    )
    stack = models.ManyToManyField(
        "vacancies.StackTool",
        related_name="vacancies",
        verbose_name="Стек",
        blank=True,
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание", blank=True, null=True)
    speciality = models.CharField(
        max_length=255,
        verbose_name="Специализация",
        choices=Speciality.choices,
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Язык программирования",
        choices=Language.choices,
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="Опыт",
        choices=Experience.choices,
    )
    grade = models.CharField(
        max_length=255,
        verbose_name="Грейд",
        choices=Grade.choices,
        blank=True,
        null=True,
    )
    is_remote = models.BooleanField(
        default=False,
        verbose_name="Можно работать удаленно",
    )
    salary_from = models.FloatField(null=True, blank=True, verbose_name="Зарплата от")
    salary_to = models.FloatField(null=True, blank=True, verbose_name="Зарплата до")
    link = models.URLField(null=True, blank=True, verbose_name="Ссылка на вакансию")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ("salary_from", "salary_to")
        unique_together = ("title", "company")

    def __str__(self):
        return self.title


class Resume(BaseModel):
    employee = models.ForeignKey(
        "users.Employee",
        on_delete=models.CASCADE,
        related_name="resumes",
        verbose_name="Работник",
    )
    position = models.CharField(max_length=255, verbose_name="Желаемая должность")
    speciality = models.CharField(
        max_length=255,
        verbose_name="Специальность",
        choices=Speciality.choices,
    )
    language = models.CharField(
        max_length=255,
        verbose_name="Основной язык программирования",
        choices=Language.choices,
    )
    stack = models.ManyToManyField(
        "vacancies.StackTool",
        related_name="resumes",
        verbose_name="Стек",
    )

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        unique_together = ("employee", "position", "speciality")

    def __str__(self):
        return self.position

    @property
    def get_experience(self):
        # TODO добавить функционал
        return self.position


class JobPlace(BaseModel):
    company = models.ForeignKey(
        "vacancies.Company",
        on_delete=models.DO_NOTHING,
        related_name="job_places",
        verbose_name="Компания",
    )
    resume = models.ForeignKey(
        "vacancies.Resume",
        on_delete=models.CASCADE,
        related_name="job_places",
        verbose_name="Резюме",
    )
    position = models.CharField(max_length=255, verbose_name="Должность")
    speciality = models.CharField(
        max_length=255,
        verbose_name="Специальность",
        choices=Speciality.choices,
    )
    job_start = models.DateField(verbose_name="Дата приема")
    job_end = models.DateField(verbose_name="Дата увольнения", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Место работы"
        verbose_name_plural = "Места работы"

    def __str__(self):
        return self.position
