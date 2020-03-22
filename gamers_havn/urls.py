from django.conf.urls import url
from django.urls import path

from gamers_havn import views


app_name = 'gamers_havn'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('about/', views.AboutView.as_view(), name='about'),
     path('game/<slug:game_title_slug>/', views.ShowGameView.as_view(), name='game'),
     path('article/<slug:article_title_slug>/', views.ShowArticleView.as_view(), name='article'),
     path('like_article/', views.LikeArticleView.as_view(), name='like_article'),
     path('edit_article/', views.EditArticleView.as_view(), name='edit_article'),
     path('goto/', views.GotoArticleView.as_view(), name='goto_article'),
     path('signup/', views.SignupView.as_view(), name='signup'),
     path('login/', views.LoginView.as_view(), name='login'),
     path('logout/', views.LogoutView.as_view(), name='logout'),
     path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
     path('change_password/<username>/', views.ChangePasswordView.as_view(), name='change_password'),
     path('created_articles/<username>/', views.CreatedArticlesView.as_view(), name='created_articles'),
     path('favorite_articles/<username>/', views.FavoriteArticlesView.as_view(), name='favorite_articles'),
     path('followed_games/<username>/', views.FollowedGamesView.as_view(), name='followed_games'),
     path('search/', views.SearchView.as_view(), name='search'),




    #  path('search/articles/', views.SearchArticlesView.as_view(), name='search_articles'),

    #  path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    #  path('category/<slug:category_name_slug>/add_page/', views.AddPageView.as_view(), 
    #       name='add_page'),
    #  path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    #  path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    #  path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
]