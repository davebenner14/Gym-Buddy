# Generated by Django 4.1.6 on 2023-02-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_plan_exercises'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='meals',
            field=models.ManyToManyField(to='main_app.meal'),
        ),
    ]
