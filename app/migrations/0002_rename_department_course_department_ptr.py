# Generated by Django 4.1.1 on 2022-10-18 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='department',
            new_name='department_ptr',
        ),
    ]