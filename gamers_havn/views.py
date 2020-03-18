from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View

from gamers_havn.models import Account, Game, Article, Tag, Comment
from gamers_havn.forms import UserForm, UserProfileForm


class IndexView(View):
    def get(self, request):
        game_list = Game.objects.order_by('-follows')[:3]
        article_list = Article.objects.order_by('-views')[:3]

        context_dict = {}
        context_dict['popular_games'] = game_list
        context_dict['popular_articles'] = article_list

        visitor_cookie_handler(request)

        return render(request, 'gamers_havn/index.html', context_dict)

class AboutView(View):
    def get(self, request):
        context_dict = {}
        visitor_cookie_handler(request)
        context_dict['visits'] = int(request.session['visits'])
        return render(request, 'gamers_havn/about.html', context_dict)

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
    
class ShowArticleView(View):
    def get(request):

        return render(request, 'gamers_havn/article.html')

class GotoArticleView(View):
    def get(self, request):
        article_id = request.GET.get('article_id')
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return redirect(reverse('gamers_havn:index'))
        article.views += 1
        article.save()

        return redirect(reverse('gamers_havn:article', kwargs={'category_name_slug': article_name_slug}))

class SignupView(View):
    def get(self, request):
        form = UserProfileForm()
        context_dict = {'form': form}
        return render(request, 'gamers_havn/signup.html', context_dict)
    
    # @method_decorator(login_required)
    # def post(self, request):
    #     form = UserProfileForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         user_profile = form.save(commit=False)
    #         user_profile.user = request.user
    #         user_profile.save()

    #         return redirect(reverse('gamers_havn:index'))
    #     else:
    #         print(form.errors)
        
    #     context_dict = {'form': form}
    #     return render(request, 'gamers_havn/.html', context_dict)

class LoginView(View):
    def get(self, request):
        form = UserProfileForm()
        context_dict = {'form': form}
        return render(request, 'gamers_havn/login.html', context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = Account.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'age': user_profile.age,
                                'portrait': user_profile.portrait})
        
        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('rango:index'))
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'gamers_havn/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('gamers_havn:index'))
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('gamers_havn:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'gamers_havn/profile.html', context_dict)


    # @method_decorator(login_required)
    # def post(self, request, game_title_slug):
    #     context_dict = self.create_context_dict(game_title_slug)
    #     query = request.POST['query'].strip()

    #     if query:
    #         context_dict['query'] = query
    #         context_dict['result_list'] = run_query(query)
        
    #     return render(request, 'gamers_havn/game.html', context_dict)


# Helper functions
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 
                                               'last_visit', 
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    
    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

# def get_game_list()