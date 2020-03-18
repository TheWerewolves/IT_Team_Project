# Generated by Django 2.2.1 on 2020-03-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers_havn', '0003_auto_20200316_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='protrait',
            new_name='portrait',
        ),
        migrations.RemoveField(
            model_name='account',
            name='favorite_article',
        ),
        migrations.RemoveField(
            model_name='account',
            name='followed_game',
        ),
        migrations.AddField(
            model_name='account',
            name='favorite_articles',
            field=models.ManyToManyField(blank=True, to='gamers_havn.Article'),
        ),
        migrations.AddField(
            model_name='account',
            name='followed_games',
            field=models.ManyToManyField(blank=True, to='gamers_havn.Game'),
        ),
    ]
