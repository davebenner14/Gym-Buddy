# Generated by Django 4.1.6 on 2023-02-15 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_comment_options_remove_comment_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]