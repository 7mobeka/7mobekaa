# Generated by Django 5.0 on 2023-12-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overall', '0002_usereventapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='application_count',
            field=models.IntegerField(default=0),
        ),
    ]
