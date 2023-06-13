# Generated by Django 4.1.3 on 2023-06-11 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0006_alter_person_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 11, 19, 42, 21, 279876, tzinfo=datetime.timezone.utc), null=True, verbose_name=' تاريخ الانضمام'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='mainunit',
            field=models.CharField(default='', max_length=200, verbose_name='الوحدة الاساسية'),
            preserve_default=False,
        ),
    ]
