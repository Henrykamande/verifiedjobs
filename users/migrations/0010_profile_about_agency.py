# Generated by Django 3.2.7 on 2021-09-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210929_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_agency',
            field=models.TextField(blank=True, null=True),
        ),
    ]