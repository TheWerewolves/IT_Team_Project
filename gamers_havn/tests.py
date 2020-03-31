from django.test import TestCase
from django.contrib.auth.models import User
from gamers_havn.models import Account, Game, Article, Comment
from django.core.validators import URLValidator
from django.urls import reverse


## test Model
class AccountTest(TestCase):

    def test_ensure_create_user(self):
        user = User.objects.create_user("testUser1", "1@gmail.com", "password")
        account = Account.objects.get_or_create(user=user)[0]
        account.save()
        self.assertEqual((account.user == user), True)

    def test_ensure_age_are_positive(self):
        account = account_creator()
        self.assertEqual((account.age >= 0), True)


class GameTest(TestCase):

    def test_slug_line_creation(self):
        title = 'Game 1'
        game = game_creator(title=title)
        game.save()
        self.assertEqual(game.slug, "game-1")

    def test_ensure_follows_are_positive(self):
        game = game_creator()
        self.assertEqual((game.follows >= 0), True)

    def test_valid_url(self):
        title = 'Game 1'
        url = "https://www.google.com/"
        game = game_creator(title=title, url=url)
        self.assertEqual(game.url, url)


class ArticleTest(TestCase):
    def test_slug_line_creation(self):
        title = "test title"
        article = article_creator(title=title)
        article.save()
        self.assertEqual(article.slug, f"{article.id}-test-title")

    def test_correct_author(self):
        author = account_creator()
        article = article_creator(author=author)
        self.assertEqual((article.author == author), True)

    def test_correct_game(self):
        game = game_creator()
        article = article_creator(game=game)
        self.assertEqual((article.game == game), True)

    def test_ensure_views_are_positive(self):
        article = article_creator()
        self.assertEqual((article.views >= 0), True)

    def test_ensure_likes_are_positive(self):
        article = article_creator()
        self.assertEqual((article.likes >= 0), True)
        

class CommentTest(TestCase):

    def test_correct_author(self):
        content = "test comment"
        article = article_creator()
        author = account_creator()
        comment = Comment(content=content, article=article, author=author)
        comment.save()
        self.assertEqual((comment.author == author), True)

    def test_correct_article(self):
        content = "test comment"
        article = article_creator()
        author = account_creator()
        comment = Comment(content=content, article=article, author=author)
        comment.save()
        self.assertEqual((comment.article == article), True)


## Test Views
### Test responses in the view
class NonLoginViewResponseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.article = article_creator()
        cls.game = game_creator()

    def test_index_response(self):
        response = self.client.get(reverse('gamers_havn:index'))
        self.assertEqual(response.status_code, 200)

    def test_about_response(self):
        response = self.client.get(reverse('gamers_havn:about'))
        self.assertEqual(response.status_code, 200)

    def test_showgame_response(self):
        response = self.client.get(reverse('gamers_havn:game', kwargs={'game_title_slug': self.game.slug}))
        self.assertEqual(response.status_code, 200)

    def test_show_article_response(self):
        response = self.client.get(reverse('gamers_havn:article', kwargs={'article_title_slug': self.article.slug}))
        self.assertEqual(response.status_code, 200)

    def test_signup_post_response(self):
        user_num = User.objects.all().count()
        response = self.client.post(reverse('gamers_havn:signup'), 
            {'username':"user1", 'email':"123456@gmail.com", 'password':"password"})
        self.assertEqual((User.objects.all().count() == user_num + 1), True)


## Helper Methods
def account_creator():
    user = User.objects.get_or_create(username="testUser1", email="1@gmail.com", password="password")[0]
    account = Account.objects.get_or_create(user=user)[0]
    account.save()
    return account

def game_creator(title='', url=''):
    if not title:
        title = 'Test Game'
    if not url:
        url = 'www.google.com'
    game = Game.objects.get_or_create(title=title, url=url)[0]
    game.save()
    return game

def article_creator(title='', author=None, game=None):
    if not title:
        title = "Test Title"
    if not author:
        author = account_creator()
    if not game:
        game = game_creator()
    article = Article.objects.get_or_create(title=title, author=author, game=game)[0]
    article.save()
    return article