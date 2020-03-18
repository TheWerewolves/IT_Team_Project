from django.conf.urls import url
from django.urls import path

from gamers_havn import views


app_name = 'gamers_havn'

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('about/', views.AboutView.as_view(), name='about'),
     path('game/<slug:game_title_slug>/', views.ShowGameView.as_view(), name='show_game'),
     path('article/<slug:article_title_slug>/', views.ShowArticleView.as_view(), name='show_article'),
     path('signup/', views.SignupView.as_view(), name='signup'),
     path('login/', views.LoginView.as_view(), name='login'),
     path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
     path('goto/', views.GotoArticleView.as_view(), name='goto_article'),
     # path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    #  path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    #  path('category/<slug:category_name_slug>/add_page/', views.AddPageView.as_view(), 
    #       name='add_page'),
    #  path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    #  path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    #  path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    #  path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
    #  path('search_add_page/', views.SearchAddPageView.as_view(), name='search_add_page'),
]