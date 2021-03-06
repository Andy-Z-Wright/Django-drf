# Generated by Django 4.0.1 on 2022-01-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Student's name", max_length=20, verbose_name='name')),
                ('age', models.SmallIntegerField(help_text="student's age", verbose_name='age')),
                ('sex', models.SmallIntegerField(choices=[(0, 'unknown'), (1, 'male'), (2, 'female')], default=0, help_text="student's sex", verbose_name='sex')),
                ('classmate', models.CharField(db_column='class', default='cs', help_text="student's calss", max_length=15, verbose_name='class')),
                ('description', models.TextField(blank=True, help_text="student's description", null=True, verbose_name='bio')),
            ],
            options={
                'verbose_name': 'student information',
                'verbose_name_plural': 'student information',
                'db_table': 'db_student',
            },
        ),
    ]
