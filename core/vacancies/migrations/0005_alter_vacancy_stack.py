# Generated by Django 5.0.3 on 2024-03-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_resume_language_alter_jobplace_speciality_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='stack',
            field=models.ManyToManyField(blank=True, related_name='vacancies', to='vacancies.stacktool', verbose_name='Стек'),
        ),
    ]
