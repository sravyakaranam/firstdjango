# Generated by Django 2.2.2 on 2019-06-21 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190620_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='senddate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 6, 21, 15, 30, 27, 46718), verbose_name='Send after'),
        ),
    ]
