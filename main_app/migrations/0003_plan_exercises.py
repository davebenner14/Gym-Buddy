# Generated by Django 4.1.6 on 2023-02-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_meal_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='exercises',
            field=models.ManyToManyField(to='main_app.exercise'),
        ),
    ]
