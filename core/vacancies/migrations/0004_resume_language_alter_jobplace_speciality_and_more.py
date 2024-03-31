# Generated by Django 5.0.3 on 2024-03-31 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_alter_vacancy_stack'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('php', 'PHP'), ('javascript', 'JavaScript'), ('cpp', 'C++'), ('csharp', 'C#'), ('java', 'Java'), ('golang', 'Go'), ('rust', 'Rust'), ('ruby', 'Ruby'), ('sql', 'SQL')], default='python', max_length=255, verbose_name='Основной язык программирования'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobplace',
            name='speciality',
            field=models.CharField(choices=[('DevOps-инженер', 'Devops'), ('Аналитик', 'Analytics'), ('Дата-сайентист', 'Data Scientist'), ('Преподаватель', 'Mentor'), ('Программист', 'Developer'), ('Руководитель группы разработки', 'Lead'), ('Системный администратор', 'System Administrator'), ('Тестировщик', 'Qa')], max_length=255, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='speciality',
            field=models.CharField(choices=[('DevOps-инженер', 'Devops'), ('Аналитик', 'Analytics'), ('Дата-сайентист', 'Data Scientist'), ('Преподаватель', 'Mentor'), ('Программист', 'Developer'), ('Руководитель группы разработки', 'Lead'), ('Системный администратор', 'System Administrator'), ('Тестировщик', 'Qa')], max_length=255, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='speciality',
            field=models.CharField(choices=[('DevOps-инженер', 'Devops'), ('Аналитик', 'Analytics'), ('Дата-сайентист', 'Data Scientist'), ('Преподаватель', 'Mentor'), ('Программист', 'Developer'), ('Руководитель группы разработки', 'Lead'), ('Системный администратор', 'System Administrator'), ('Тестировщик', 'Qa')], max_length=255, verbose_name='Специализация'),
        ),
    ]