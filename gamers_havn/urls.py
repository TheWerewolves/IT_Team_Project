from django.conf.urls import url
from django.urls import path

from gamers_havn import views


app_name = 'gamers_havn'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('about/', views.AboutView.as_view(), name='about'),
     path('game/<slug:game_title_slug>/', views.ShowGameView.as_view(), name='game'),
     path('follow_game/', views.FollowGameView.as_view(), name='follow_game'),
     path('game_list_article/', views.GameListArticleView.as_view(), name='game_list_article'),
     path('article/<slug:article_title_slug>/', views.ShowArticleView.as_view(), name='article'),
     path('like_article/', views.LikeArticleView.as_view(), name='like_article'),
     path('edit_article/', views.EditArticleView.as_view(), name='edit_article'),
     path('goto/', views.GotoArticleView.as_view(), name='goto_article'),
     path('signup/', views.SignupView.as_view(), name='signup'),
     path('login/', views.LoginView.as_view(), name='login'),
     path('login_with_social/', views.LoginWithSocialView.as_view(), name='login_with_social'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
     path('change_password/<username>/', views.ChangePasswordView.as_view(), name='change_password'),
     path('created_articles/<username>/', views.CreatedArticlesView.as_view(), name='created_articles'),
     path('favorite_articles/<username>/', views.FavoriteArticlesView.as_view(), name='favorite_articles'),
     path('followed_games/<username>/', views.FollowedGamesView.as_view(), name='followed_games'),
     path('search/', views.SearchView.as_view(), name='search'),
]