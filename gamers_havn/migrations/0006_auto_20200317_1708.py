# Generated by Django 2.2.1 on 2020-03-17 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gamers_havn', '0005_auto_20200317_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 17, 17, 8, 59, 100445, tzinfo=utc)),
        ),
    ]