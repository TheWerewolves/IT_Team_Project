from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Account(models.Model):

    # Include id, name, e-mail, user permission and much more
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField(default=0)
    portrait = models.ImageField(upload_to='profile_images', blank=True)
    favorite_articles = models.ManyToManyField('Article', blank=True)
    followed_games = models.ManyToManyField('Game', blank=True)

    def __str__(self):
        return self.user.username


class Game(models.Model):

    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique=True)
    follows = models.IntegerField(default=0)
    url = models.URLField()
    tags = models.ManyToManyField('Tag', limit_choices_to={'is_game_tag': True})
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug =  slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):

    TITLE_MAX_LENGTH = 128

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    content = models.FileField(upload_to='articles')
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = f"{self.id}-{slugify(self.title)}"
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):

    TAG_MAX_LENGTH = 64

    tag = models.CharField(max_length=TAG_MAX_LENGTH, unique=True)
    is_game_tag = models.BooleanField(default=False)

    def __str__(self):
        return self.tag


class Comment(models.Model):

    CONTENT_MAX_LENGTH = 256

    content = models.CharField(max_length=CONTENT_MAX_LENGTH)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}'s comment about {self.article}"

