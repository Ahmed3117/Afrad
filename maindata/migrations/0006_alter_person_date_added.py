# Generated by Django 4.2 on 2023-06-02 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0005_rename_main_unit_person_mainunit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 2, 10, 6, 46, 250425, tzinfo=datetime.timezone.utc), null=True, verbose_name=' تاريخ الانضمام'),
        ),
    ]
