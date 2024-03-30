# Generated by Django 5.0.3 on 2024-03-30 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='StackTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Стек',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='companies', to='vacancies.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('name',),
                'unique_together': {('city', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(max_length=255, verbose_name='Желаемая должность')),
                ('speciality', models.CharField(max_length=255, verbose_name='Специальность')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='users.employee', verbose_name='Работник')),
                ('stack', models.ManyToManyField(related_name='resumes', to='vacancies.stacktool', verbose_name='Стек')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'unique_together': {('employee', 'position', 'speciality')},
            },
        ),
        migrations.CreateModel(
            name='JobPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('speciality', models.CharField(max_length=255, verbose_name='Специальность')),
                ('job_start', models.DateField(verbose_name='Дата приема')),
                ('job_end', models.DateField(blank=True, null=True, verbose_name='Дата увольнения')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='job_places', to='vacancies.company', verbose_name='Компания')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_places', to='vacancies.resume', verbose_name='Резюме')),
            ],
            options={
                'verbose_name': 'Место работы',
                'verbose_name_plural': 'Места работы',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('speciality', models.CharField(max_length=255, verbose_name='Специализация')),
                ('language', models.CharField(choices=[('python', 'Python'), ('php', 'PHP'), ('javascript', 'JavaScript'), ('cpp', 'C++'), ('csharp', 'C#'), ('java', 'Java'), ('golang', 'Go'), ('rust', 'Rust'), ('ruby', 'Ruby'), ('sql', 'SQL')], max_length=255, verbose_name='Язык программирования')),
                ('experience', models.CharField(choices=[('no_experience', 'Без опыта'), ('between_1_2', 'От 1 до 3 лет'), ('between_3_5', 'От 3 до 5 лет'), ('more_than_5', 'Более 5 лет')], max_length=255, verbose_name='Опыт')),
                ('grade', models.CharField(blank=True, choices=[('trainee', 'Стажер'), ('junior', 'Джуниор'), ('middle', 'Миддл'), ('senior', 'Сеньор'), ('lead', 'Лид')], max_length=255, null=True, verbose_name='Грейд')),
                ('salary_from', models.FloatField(blank=True, null=True, verbose_name='Зарплата от')),
                ('salary_to', models.FloatField(blank=True, null=True, verbose_name='Зарплата до')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.company', verbose_name='Компания')),
                ('stack', models.ManyToManyField(related_name='vacancies', to='vacancies.stacktool', verbose_name='Стек')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ('salary_from', 'salary_to'),
                'unique_together': {('title', 'company')},
            },
        ),
    ]
