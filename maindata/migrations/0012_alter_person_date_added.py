# Generated by Django 4.1.3 on 2023-06-13 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0011_alter_holiday_date_from_alter_holiday_date_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 13, 11, 12, 33, 870874, tzinfo=datetime.timezone.utc), null=True, verbose_name=' تاريخ الانضمام'),
        ),
    ]
