# Generated by Django 4.1.6 on 2023-02-14 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_plan_exercises_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='plan',
        ),
        migrations.AddField(
            model_name='comment',
            name='exercise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.exercise'),
            preserve_default=False,
        ),
    ]