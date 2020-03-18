import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Team_Project.settings')

import django
django.setup()

from django.contrib.auth.models import User

from django.core.files import File
from django.core.files.images import ImageFile

from gamers_havn.models import Account, Game, Article, Tag, Comment


def populate():

    accounts = [
        {
            'user': {
                'username': 'yuuto', 'password': 'password',
                'email': 'yuuto@mymail.com',
            },
            'age': 15, 'portrait': f'profile_images/Golurk.png'
        },
        {
            'user': {
                'username': 'benny', 'password': 'password',
                'email': 'benny@mymail.com',
            },
            'age': 16, 'portrait': f'profile_images/Golurk.png'
        },
    ]

    games = [
        {'title': 'League of Legends',
         'url': 'https://euw.leagueoflegends.com/en-gb/'},
        {'title': 'Overwatch',
         'url': 'https://playoverwatch.com/en-us/'},
        {'title': "Playerunknown's Battleground",
         'url': 'https://www.pubg.com/'},
        {'title': 'Dark Souls',
         'url': 'https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/'},
    ]

    articles = [
        {'title': "Master LoL's Teamfight Tactics mode with these top tips",
         'content': 'a1.txt',
         'author': 'yuuto',
         'game': 'League of Legends'
        },
        {'title': "QUICK LOL THOUGHTS",
         'content': 'a2.txt',
         'author': 'benny',
         'game': 'League of Legends'
        },
        {'title': "This is how i play PUBG",
         'content': 'a1.txt',
         'author': 'yuuto',
         'game': 'League of Legends'
        },
    ]

    for account in accounts:
        add_account(account['user']['username'], account['user']['email'],
                    account['user']['password'], account['age'], account['portrait'])

    for game in games:
        add_game(game['title'], game['url'])

    for article in articles:
        user = User.objects.filter(username=article['author'])[0]
        account = Account.objects.filter(user=user)[0]
        game = Game.objects.filter(title=article['game'])[0]
        content = f"articles/{game.slug}/{article['content']}"
        add_article(article['title'], content, account, game)


def add_account(name, email, password, age, portrait):
    user = User.objects.get_or_create(username=name, email=email, password=password)[0]
    account = Account.objects.get_or_create(user=user)[0]
    account.age = age
    account.portrait = portrait
    account.save()

def add_game(title, url):
    g = Game.objects.get_or_create(title=title, url=url)[0]
    g.save()

def add_article(title, content, author, game):
    a = Article.objects.get_or_create(title=title, content=content, 
                                      author=author, game=game)[0]
    a.save()


if __name__ == '__main__':
    print("Starting Gamer's Havn population script...")
    populate()
