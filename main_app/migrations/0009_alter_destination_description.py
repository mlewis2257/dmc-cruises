# Generated by Django 4.2.5 on 2023-09-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_cruise_picturepath_destination_picturepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(default='', max_length=3000),
        ),
    ]
