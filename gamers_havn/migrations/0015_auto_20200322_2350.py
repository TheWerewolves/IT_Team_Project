# Generated by Django 2.2.1 on 2020-03-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers_havn', '0014_auto_20200322_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.FileField(upload_to='articles'),
        ),
    ]