import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'IT_Team_Project.settings')

import django
django.setup()

from django.contrib.auth.models import User

from gamers_havn.models import Account, Game, Article


def populate():

    accounts = [
        {
            'user': {
                'username': 'yuuto', 'password': 'pw000000',
                'email': 'yuuto@mymail.com',
            },
            'age': 15
        },
        {
            'user': {
                'username': 'Benny', 'password': 'pw000000',
                'email': 'benny@mymail.com',
            },
            'age': 16
        },
        {
            'user': {
                'username': 'baobao', 'password': 'pw000000',
                'email': 'baobao@mymail.com',
            },
            'age': 10
        },
        {
            'user': {
                'username': 'BBLover', 'password': 'pw000000',
                'email': 'blackopiumlover@mymail.com',
            },
            'age': 1
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
        {'title': 'Minecraft',
         'url': 'https://minecraft.net/'},
        {'title': 'Teamfight Tactic',
         'url': 'https://teamfighttactics.leagueoflegends.com/en-gb/'},
        {'title': 'Call of Duty: Modern Warfare',
         'url': 'https://www.callofduty.com/modernwarfare'},
        {'title': 'Hearthstone',
         'url': 'https://playhearthstone.com/en-gb/'},
        {'title': 'World of Warcraft',
         'url': 'https://worldofwarcraft.com/'},
        {'title': 'Grand Theft Auto V',
         'url': 'https://www.rockstargames.com/V/'},
         {'title': 'Battlefield 4',
         'url': 'https://www.ea.com/games/battlefield/battlefield-4'},
    ]

    articles = [
        {'title': "League Of Legends One For All Mode Returns",
         'content': '''
##After two years in limbo, One For All returns to League of Legends for a limited time.
One For All is making a surprise comeback to Riot's League of Legends in patch 10.6. Previously, One For All was an arcade game mode wherein both opposing teams only have one champion each, with players needing to work together to take on the other team's single champion.

As you can imagine, having to work together in League of Legends is an ambitious notion, much less putting five players in control of the same champion at once and expecting a competent level of cooperation. Nevertheless, Riot is set on bringing the arcade mode back after a two-year absence, although only for a limited time.

The last time we saw One For All was April Fools Day in 2018. Since then, League of Legends has added eight new champions and been through a number of patches and balance changes. How this will affect One For All is yet to be seen, but some interesting strategies are sure to emerge from the game mode.

Original One For All strategies aren¡¯t completely unusable, but older strategies are sure to resurface with the reemergence of the game mode. Ultimately it may even come down to old vs new in the first week of release.

Riot has promised to keep a close eye on the game mode, checking that no one champion becomes too over or underpowered in the mode. The whole point of One For All is cooperation, not just picking a strong champion every round. Balancing will be similar to the already existing changes on ARAM and URF.

One For All is currently available to play on the Public Beta Environment (PBE) and will go live alongside Patch 10.6 on March 18. League of Legends' Arcade games generally stick around for at least two patches, so check it out before the mode disappears again.

*Notice: This article is originally From https://www.gamespot.com/articles/league-of-legends-one-for-all-mode-returns/1100-6474417// The poster in our website do not own the articles*
                    ''',
         'author': 'yuuto',
         'game': 'League of Legends'},

         {'title': "DARK SOULS 3 GUIDE",
         'content': '''
Dark Souls 3 is here, and From Software's notoriously difficult action role-playing game series is bigger than it's ever been.

We've scoured every inch of the Kingdom of Lothric to help you uncover its mysteries and overcome odds stacked to beat you down. We've organized our guide into a few different sections, based on what you might need at any given moment.

If you're just starting out, be sure to read through our Beginner's Guide, which will teach new and experienced players what you should know in your first hours. Lothric is brutal, and this will help you overcome seemingly insurmountable odds. And we'll teach you how to build the best character we've ever built in a Souls game.

Our full walkthrough of the game begins with the enemies, items and secrets in the Cemetery of Ash and Firelink Shrine. Then it guides you through all of the the areas you'll visit in Dark Souls 3, from the required to the optional and secret ¡ª and there's more than a few of the latter. Stuck on a boss? Just visit the section it appears in, and you'll find strategies and videos.

From its earliest days, the Dark Souls series asked players to prepare to die. We've done that plenty. We suspect you will, too. But with Polygon's Dark Souls 3 guide by your side, you can prepare to die a lot less than you otherwise would have.

![](https://cdn2.vox-cdn.com/uploads/chorus_asset/file/6322727/Fire_Keeper.0.jpg)

![](https://cdn0.vox-cdn.com/uploads/chorus_asset/file/7783887/2016-04-10_Firelink_Shrine_Interior_TOC.0.png)

Dark Souls 3's maps are a confusing, intriguing mass of overlapping spaghetti. But with this guide, you'll be able to find your place ¡ª as well as every enemy and item ¡ª on every map. You'll also find links to every part of Polygon's full walkthrough, so you can find your way to where you need to be.

![](https://cdn0.vox-cdn.com/uploads/chorus_image/image/49740339/Firelink_Tower_header_image.0.0.jpg)

![](https://cdn2.vox-cdn.com/uploads/chorus_asset/file/6323259/Iudex_Gundyr.0.jpg)

What class should you choose? What starting item? Our guide will make your first dozen hours in Lothric much easier. Think of this as a way to learn the language of Dark Souls 3 without cheating ¡ª or a way to even the odds in a game where you're always outnumbered, always outgunned.

![](https://cdn0.vox-cdn.com/uploads/chorus_image/image/49740339/Firelink_Tower_header_image.0.0.jpg)

You'll see most of Dark Souls 3 as you progress through its bonfires, but there are a few hidden, optional areas reserved for the most daring players. Most have challenging foes. Some end with optional boss fights. All of them balance out the difficulty with great rewards.

![](https://cdn0.vox-cdn.com/uploads/chorus_asset/file/6363563/Online_header_image.0.jpg)

*Notice: This article is originally From https://www.polygon.com/2016/4/12/11412098/dark-souls-3-guide The poster in our website do not own the articles*
                    ''',
         'author': 'yuuto',
         'game': 'Dark Souls'},

         {'title': "Overwatch Adds A New Doomfist Legendary Skin For A Limited Time",
         'content': '''
## Overwatch has a new Doomfist skin on PC, PS4, Xbox One, and Switch in honor of Overwatch League Season 2 MVP Jay "Sinatraa" Won
The Overwatch League has revealed a new legendary skin for Blizzard's hero shooter. The skin is for Doomfist and is called Thunder, and it's in celebration of one of its most important players. You can see it in the tweet embedded below.

![](https://pbs.twimg.com/media/ET46HncUMAAwJxf?format=jpg&name=small)

Thunder will only be available for purchase in-game for a limited-time, becoming available from March 26 through April 9. The skin is in celebration of the professional esports player Jay "Sinatraa" Won, a member of esports team Shock, who won the Overwatch League Season 2 MVP award. Sinatraa is Shock's resident DPS player and has regularly used Doomfist during the Overwatch League.
Overwatch is set to get one more new hero before the release of Overwatch 2. First teased in animated shorts, Echo will be joining the hero shooter as another DPS fighter (Blizzard has followed up to tell fans to not worry, more support and tank heroes are in development).

Originally conceived for Blizzard's cancelled Titan project, Echo is a versatile hero--able to mimic the forms and abilities of any other character. In describing Echo, GameSpot editor Phil Hornshaw writes, "Key to Echo is her adaptability, and from what Goodman and Fonville described, players who try out the new hero should have a lot of chances to find creative ways to use her abilities. The character's versatility means she can be used to control territory with sticky bombs, as a straight damage-dealer using sticky bombs and Focusing Beam, or to shore up a team in an emergency by duplicating other characters. We'll have to wait to see what other creative ways players find to use Echo--and to counter her."

If you're looking to have a go at Echo early, the hero is live on Overwatch's Public Test Realm right now.

*Notice: This article is originally From https://www.gamespot.com/articles/overwatch-adds-a-new-doomfist-legendary-skin-for-a/1100-6475184/ The poster in our website do not own the articles*
                    ''',
         'author': 'Benny',
         'game': 'Overwatch'},

         {'title': "How to Play Nasus in League of Legends",
         'content': '''
Nasus is a melee Fighter, Tank and Mage who excels in Solo Top and in the Jungle. His skins are Galactic Nasus, Pharaoh Nasus, Dreadknight Nasus, Riot K9 Nasus and Infernal Nasus.
##1 Leveling and Abilities

![](https://www.wikihow.com/images/thumb/a/a2/Play-Nasus-in-League-of-Legends-Step-1.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-1.jpg.webp)

###1 Learn the abilities.
Passive (Soul Eater) Nasus has life steal for his attacks  
Q (Siphoning Strike) Nasus' axe is empowered and his next basic attack will deal bonus damage. If Siphoning Strike kills a unit, it will gain stacks of Siphoning Strike which will permanently deal more damage on usage of Siphoning Strike.  
W (Wither) Nasus slows an enemy champion for 5 seconds. The slow percentage increases over time.  
E (Spirit Fire) Nasus puts a spirit flame in a circular area. This deals magic damage and reduces foes' armor every second. This has a high mana cost so make sure you don't use it too often.  
R (Fury of the Sands) Nasus transforms into a big version and increases damage, life steal and attack range. This also gives a massive health boost. Enemies near Nasus are damaged by a percentage of their maximum health. Siphoning Strike deals extra damage in this duration too. Nasus turns back into his normal form after a few seconds.

![](https://www.wikihow.com/images/thumb/b/b1/Play-Nasus-in-League-of-Legends-Step-2.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-2.jpg.webp)

###2 
Level up as follows:
Take Siphoning Strike at Level one and max it immediately. 
Take Wither at Level two and max it second. 
Take Spirit Fire at Level four and max it last. 
Take Fury of the Sands at level six, eleven and sixteen.
##2 Build Guide

![](https://www.wikihow.com/images/thumb/3/32/Play-Nasus-in-League-of-Legends-Step-3.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-3.jpg.webp)

###1 Use the following recommendations for starts: Doran's Shield, Amplifying Tone, Cloth Armor, Ancient Coin or Boots of Speed.

![](https://www.wikihow.com/images/thumb/5/54/Play-Nasus-in-League-of-Legends-Step-4.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-4.jpg.webp)

###2 Use the following recommendations for mid game: Iceborn Gauntlet, Frozen Heart, Rylai's Crystal Scepter, Seeker's Armguard, and Ninja Tabi.
As long as you focus ability power, mana and armor, you are fine.

![](https://www.wikihow.com/images/thumb/1/14/Play-Nasus-in-League-of-Legends-Step-5.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-5.jpg.webp)

###3 Get masteries. Take all armor and magic resist masteries as well as ability power masteries.

![](https://www.wikihow.com/images/thumb/e/e8/Play-Nasus-in-League-of-Legends-Step-6.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-6.jpg.webp)

###4 Get runes. Focus on ability power and mana.

![](https://www.wikihow.com/images/thumb/6/69/Play-Nasus-in-League-of-Legends-Step-7.jpg/aid5674065-v4-728px-Play-Nasus-in-League-of-Legends-Step-7.jpg.webp)

###5 Get flash. It is a must take for summoner spells. Teleport and Ignite are also good choices. Take smite for jungling.

*Notice: This article is originally From https://https://www.wikihow.com/Play-Nasus-in-League-of-Legends/ The poster in our website do not own the articles*
                    ''',
         'author': 'baobao',
         'game': 'League of Legends'},
    ]

    for account in accounts:
        add_account(account['user']['username'], account['user']['email'],
                    account['user']['password'], account['age'])

    for game in games:
        add_game(game['title'], game['url'])

    for article in articles:
        account = Account.objects.get(user__username=article['author'])
        game = Game.objects.get(title=article['game'])
        content = article['content']
        add_article(article['title'], content, account, game)


def add_account(name, email, password, age, portrait=None):
    user = User.objects.get_or_create(username=name, email=email, password=password)[0]
    account = Account.objects.get_or_create(user=user)[0]
    account.age = age
    account.portrait = portrait
    account.save()
    print(f"Added user {user}")

def add_game(title, url):
    g = Game.objects.get_or_create(title=title)[0]
    g.url = url
    g.save()
    print(f"Added game '{g}'")

def add_article(title, content, author, game):
    try:
        a = Article.objects.get(title=title)
        a.content = content
        a.author = author
        a.game = game
        a.save()
    except:
        a = Article.objects.create(title=title, content=content, author=author, game=game)
    
    print(f"Added article '{a}'")


if __name__ == '__main__':
    print("Starting Gamer's Havn population script...")
    populate()
