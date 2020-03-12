from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Account(models.Model):

    # Include id, name, e-mail, user permission and much more
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.IntegerField(default=0)
    protrait = models.ImageField(upload_to='profile_images', blank=True)
    favorite_article = models.ManyToManyField(
        Article, 
        related_name='favorite_article',
        blank=True,
        null=True
    )
    followed_game = models.ManyToManyField(
        Game, 
        related_name='followed_game',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class Game(models.Model):

    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    follows = models.IntegerField(default=0)
    url = models.URLField()
    tags = models.ManyToManyField(Tag, limit_choices_to={'is_game_tag': True})
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(models.Model):

    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    comments = models.ManyToManyField(Comment)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):

    TAG_MAX_LENGTH = 64

    tag = models.CharField(max_length=TAG_MAX_LENGTH)
    is_game_tag = models.BooleanField(default=False)

    def __str__(self):
        return self.tag


class Comment(models.Model):

    CONTENT_MAX_LENGTH = 256

    content = models.CharField(max_length=CONTENT_MAX_LENGTH)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"{author}'s comment about {article}"