# Generated by Django 3.1.2 on 2020-10-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_auto_20201028_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='Latitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='place',
            name='Loggitude',
            field=models.CharField(max_length=50),
        ),
    ]