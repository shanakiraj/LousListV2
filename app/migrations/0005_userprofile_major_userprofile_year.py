# Generated by Django 4.1.1 on 2022-12-07 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='major',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
