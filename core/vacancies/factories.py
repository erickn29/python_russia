from django.conf import settings

import factory

from faker import Faker

from vacancies.models import StackTool, City, Company, Vacancy

fake = Faker(settings.LANGUAGE_CODE)
Faker.seed(2)


class StackToolFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StackTool

    name = fake.numerify("#" * 5)


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = fake.city()


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    city = factory.SubFactory(CityFactory)
    name = fake.company()


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vacancy

    company = factory.SubFactory(CompanyFactory)
    title = fake.word()
    speciality = fake.word()
    language = fake.word()
    experience = fake.word()
    grade = fake.word()
    salary_from = fake.pyfloat(5, 1, True)
    salary_to = fake.pyfloat(6, 1, True)
    link = fake.url()
    is_remote = fake.boolean()
