# Generated by Django 3.2.7 on 2021-10-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_countries'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='countries',
            field=models.ManyToManyField(blank=True, to='projects.Countries'),
        ),
    ]
