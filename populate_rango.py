import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Team_Project.settings')

import django
django.setup()

from gamers_havn.models import Account, Game, Article, Tag, Comment


def populate():

    pass

if __name__ == '__main__':
    print("Starting Gamer's Havn population script...")
    populate()
