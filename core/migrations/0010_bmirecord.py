# Generated by Django 5.0.2 on 2024-03-13 17:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_exercise_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMIRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.FloatField(help_text='Height in meters')),
                ('weight', models.FloatField(help_text='Weight in kilograms')),
                ('age', models.PositiveIntegerField()),
                ('bmi', models.FloatField(help_text='Body Mass Index')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
