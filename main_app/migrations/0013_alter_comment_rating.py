# Generated by Django 4.1.6 on 2023-02-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_review_product_remove_exercise_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
