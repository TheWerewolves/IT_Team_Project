from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.db.models import Q

from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from gamers_havn.models import Account, Game, Article, Comment
from gamers_havn.forms import UserForm, UserProfileForm


class IndexView(View):
    def get(self, request):
        game_list = Game.objects.order_by('-follows')[:3]
        article_list = Article.objects.order_by('-views')[:3]

        context_dict = {}
        context_dict['popular_games'] = game_list
        context_dict['popular_articles'] = article_list

        return render(request, 'gamers_havn/index.html', context_dict)

class AboutView(View):
    def get(self, request):
        return render(request, 'gamers_havn/about.html')

class ShowGameView(View):
    def create_context_dict(self, game_title_slug):
        context_dict = {}
        try:
            game = Game.objects.get(slug=game_title_slug)
            articles = Article.objects.filter(game=game).order_by('-views')
            context_dict['game'] = game
            context_dict['articles'] = articles
        except Game.DoesNotExist:
            context_dict['game'] = None
            context_dict['articles'] = None
        return context_dict
    
    def get(self, request, game_title_slug):
        context_dict = self.create_context_dict(game_title_slug)
        return render(request, 'gamers_havn/game.html', context_dict)

class FollowGameView(View):
    @method_decorator(login_required)
    def get(self, request):
        game_id = request.GET['game_id']
        button = request.GET['button']

        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return HttpResponse(False)

        account = get_current_account(request)

        if button == 'Follow':
            account.followed_games.add(game)
        else:
            account.followed_games.remove(game)

        account.save()
        game.save()

        return HttpResponse(True)

# Called when user hit order by button to request different ordered articles of a game
class GameListArticleView(View):
    def get(self, request):
        order_by = request.GET['orderby']
        game_id = request.GET['game_id']

        articles = None
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return None

        if 'Views' in order_by:
            articles = Article.objects.filter(game=game).order_by('-views')
        elif 'Likes' in order_by:
            articles = Article.objects.filter(game=game).order_by('-likes')
        elif 'Date' in order_by:
            articles = Article.objects.filter(game=game).order_by('-created_at')

        return render(request, 'gamers_havn/article_list.html', {'articles': articles})

class ShowArticleView(View):
    def get(self, request, article_title_slug):
        try:
            article = Article.objects.get(slug=article_title_slug)
            comments = Comment.objects.filter(article=article)
        except Article.DoesNotExist:
            article = None
            comments = None

        account = get_current_account(request)
        is_liked = False
        if account and article in account.favorite_articles.all():
            is_liked = True

        context_dict = {}
        context_dict['article'] = article
        context_dict['game'] = article.game
        context_dict['comments'] = comments
        context_dict['is_liked'] = is_liked

        return render(request, 'gamers_havn/article.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, article_title_slug):
        comment_content = request.POST['comment']

        try:
            article = Article.objects.get(slug=article_title_slug)
            author = get_current_account(request)
        except Article.DoesNotExist:
            redirect(reverse('gamers_havn:index'))

        comment = Comment(content=comment_content, author=author, article=article)
        comment.save()

        context_dict = {}
        context_dict['article'] = article

        return redirect(reverse('gamers_havn:article', kwargs={'article_title_slug': article.slug}))

class LikeArticleView(View):
    @method_decorator(login_required)
    def get(self, request):
        article_id = request.GET['article_id']
        button = request.GET['button']

        try:
            article = Article.objects.get(id=int(article_id))
        except Article.DoesNotExist or Account.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        account = get_current_account(request)

        if button == 'Like':
            account.favorite_articles.add(article)
        else:
            account.favorite_articles.remove(article)
        account.save()
        article.save()

        return HttpResponse(article.likes)

# Called when a user request to view an article
class GotoArticleView(View):
    def get(self, request):
        article_id = request.GET.get('article_id')
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return redirect(reverse('gamers_havn:index'))
        article.views += 1
        article.save()

        return redirect(reverse('gamers_havn:article', kwargs={'article_title_slug': article.slug}))

class SignupView(View):
    def get(self, request):
        user_list = User.objects.all().values_list('username', flat=True)
        context_dict = {'user_list': user_list}
        return render(request, 'gamers_havn/signup.html', context_dict)

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            account = Account.objects.create(user=user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('gamers_havn:index'))

        context_dict = {}
        context_dict['username'] = username
        context_dict['email'] = email
        context_dict['password'] = password
        return render(request, 'gamers_havn/signup.html', context_dict)

class LoginView(View):
    def get(self, request):
        return render(request, 'gamers_havn/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse('gamers_havn:index'))
        
        context_dict = {}
        context_dict['username'] = username
        context_dict['password'] = password
        return render(request, 'gamers_havn/login.html', context_dict)

class LoginWithSocialView(View):
    def get(self, request):
        user = request.user
        account = Account.objects.get_or_create(user=user)

        if not user.has_usable_password():
            return redirect(reverse('gamers_havn:change_password', kwargs={'username': user.username}))
        
        return redirect(reverse('gamers_havn:index'))

class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect(reverse('gamers_havn:index'))

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            user_profile = get_user_details(username)
        except TypeError:
            return redirect(reverse('gamers_havn:index'))

        return render(request, 'gamers_havn/profile.html', {'user_profile': user_profile})
    
    @method_decorator(login_required)
    def post(self, request, username):
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        portrait = request.FILES.get('portrait', None)

        try:
            user_profile = get_user_details(username)
        except TypeError:
            return redirect(reverse('gamers_havn:index'))

        if user_profile.user.username == username or len(User.objects.filter(username=username)) == 0:
            user_profile.user.username = username
            if email:
                user_profile.user.email = email
            if age:
                user_profile.age = age
            if portrait:
                user_profile.portrait = portrait

            user_profile.user.save()
            user_profile.save()
            return redirect(reverse('gamers_havn:profile', kwargs={'username': username}))

        return render(request, 'gamers_havn/profile.html', {'user_profile': user_profile, 'changed_name': username})

class ChangePasswordView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            user_profile = get_user_details(username)
        except TypeError:
            return redirect(reverse('gamers_havn:index'))

        context_dict = {}
        context_dict['user_profile'] = user_profile

        if not request.user.has_usable_password():
            context_dict['change_pw_message'] = "You don't have a password yet, set it here to login next time!"

        return render(request, 'gamers_havn/change_password.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        old_password = ''
        if 'old_password' in request.POST:
            old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        try:
            user_profile = get_user_details(username)
            user = user_profile.user
        except TypeError:
            return redirect(reverse('gamers_havn:index'))

        change_pw_message = ''
        if check_password(old_password, user.password) or not user.has_usable_password():
            if new_password == confirm_password:
                user.password = make_password(new_password)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(reverse('gamers_havn:index'))
            else:
                change_pw_message = 'The confirmation did not match, Please try again.'
        else:
            change_pw_message = 'Old password is incorrect, Please try again.'
        
        context_dict = {}
        context_dict['user_profile'] = user_profile
        context_dict['change_pw_message'] = change_pw_message

        return render(request, 'gamers_havn/change_password.html', context_dict)

class CreatedArticlesView(View):
    def get(self, request, username):
        try:
            user_profile = get_user_details(username)
        except TypeError:
            return redirect(reverse('gamers_havn:index'))
        article_list = Article.objects.filter(author__user__username=username)
        context_dict = {}
        context_dict['user_profile'] = user_profile
        context_dict['articles'] = article_list
        return render(request, 'gamers_havn/created_articles.html', context_dict)

class FavoriteArticlesView(View):
    def get(self, request, username):
        try:
            user_profile = get_user_details(username)
            article_list = user_profile.favorite_articles.all()
        except TypeError:
            return redirect(reverse('gamers_havn:index'))
        context_dict = {}
        context_dict['user_profile'] = user_profile
        context_dict['articles'] = article_list
        return render(request, 'gamers_havn/favorite_articles.html', context_dict)

class FollowedGamesView(View):
    def get(self, request, username):
        try:
            user_profile = get_user_details(username)
            game_list = user_profile.followed_games.all()
            for game in game_list:
                game.articles = Article.objects.filter(game__title=game.title).count()
        except TypeError:
            return redirect(reverse('gamers_havn:index'))
        context_dict = {}
        context_dict['user_profile'] = user_profile
        context_dict['games'] = game_list
        return render(request, 'gamers_havn/followed_games.html', context_dict)

class SearchView(View):
    def get(self, request):
        return render(request, 'gamers_havn/search.html')

    def post(self, request):
        search_query = request.POST['search_query']
        search_type = request.POST['search_type']
        context_dict = {}

        if search_type == 'Articles':
            context_dict['articles'] = get_article_list(max_result=0, query=search_query)
        elif search_type == 'Games':
            context_dict['games'] = get_game_list(max_result=0, query=search_query)
        elif search_type == 'Users':
            context_dict['users'] = get_user_list(max_result=0, query=search_query)

        context_dict['search_query'] = search_query

        return render(request, 'gamers_havn/search.html', context_dict)

class EditArticleView(View):
    @method_decorator(login_required)
    def get(self, request):
        context_dict = {}
        games = Game.objects.all()
        context_dict['games'] = games

        if 'article_id' in request.GET:
            article_id = request.GET['article_id']
            article = Article.objects.get(id=int(article_id))
            context_dict['article'] = article
        elif 'game_id' in request.GET:
            game_id = request.GET['game_id']
            game = Game.objects.get(id=int(game_id))
            context_dict['game'] = game

        return render(request, 'gamers_havn/edit_article.html', context_dict)

    @method_decorator(login_required)
    def post(self, request):
        id = request.POST['id']
        title = request.POST['title']
        game_title = request.POST['game_title']
        content = request.POST['content']

        try:
            author = get_current_account(request)
            game = Game.objects.get(title=game_title)
        except Game.DoesNotExist or Account.DoesNotExist:
            return HttpResponse(reverse('gamers_havn:index'))

        try:
            article = Article.objects.get(id=id)
            article.title = title
            article.author = author
            article.game = game
            article.content = content
        except Article.DoesNotExist:
            article = Article.objects.create(title=title, author=author, game=game, content=content)
        
        article.save()

        return HttpResponse(reverse('gamers_havn:article', kwargs={'article_title_slug': article.slug}))


# Helper functions
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def get_article_list(max_result=0, query=''):
    article_list = []
    if len(query) > 0:
        article_list = Article.objects.filter(
            Q(title__icontains=query) | Q(author__user__username__icontains=query) | Q(game__title__icontains=query) | Q(content__icontains=query)
        )
    else:
        article_list = Article.objects.all()
    if max_result > 0:
        if len(article_list) > max_result:
            article_list = article_list[:max_result]
    return article_list

def get_game_list(max_result=0, query=''):
    game_list = []
    if len(query) > 0:
        game_list = Game.objects.filter(title__icontains=query)
    else:
        game_list = Game.objects.all()

    for game in game_list:
            game.articles = Article.objects.filter(game__title=game.title).count()
            
    if max_result > 0:
        if len(game_list) > max_result:
            game_list = game_list[:max_result]
    return game_list

def get_user_list(max_result=0, query=''):
    user_list = []
    if len(query) > 0:
        user_list = Account.objects.filter(user__username__icontains=query)
    else:
        user_list = Account.objects.all()
    if max_result > 0:
        if len(user_list) > max_result:
            user_list = user_list[:max_result]
    return user_list

def get_user_details(username):
    user_profile = Account.objects.get_or_create(user__username=username)[0]
    return user_profile

def get_current_account(request):
    account = None
    if request.user.is_authenticated:
        account = Account.objects.get_or_create(user=request.user)[0]
    return account
