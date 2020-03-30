import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.deconstruct import deconstructible

from uuid import uuid4

# Helpers
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = os.path.splitext(filename)[-1]
        filename = '{}{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


# Models
class Account(models.Model):

    # Include id, name, e-mail, user permission and much more
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField(default=0)
    portrait = models.ImageField(upload_to=PathAndRename('profile_images'), blank=True)
    favorite_articles = models.ManyToManyField('Article', blank=True)
    followed_games = models.ManyToManyField('Game', blank=True)

    def __str__(self):
        return self.user.username


class Game(models.Model):

    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    follows = models.IntegerField(default=0)
    url = models.URLField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.title)
        self.follows = self.account_set.count()
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):

    TITLE_MAX_LENGTH = 128

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            a = Article.objects.order_by('-id').first()
            if not a:
                self.id = 0
            else:
                self.id = a.id + 1
        self.slug = f"{self.id}-{slugify(self.title)}"
        self.likes = self.account_set.count()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):

    CONTENT_MAX_LENGTH = 256

    content = models.CharField(max_length=CONTENT_MAX_LENGTH)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s comment about {self.article}"


