# Generated by Django 2.2.2 on 2019-06-22 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190622_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='senddate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 22, 15, 1, 57, 803555), verbose_name='Send after'),
        ),
    ]
