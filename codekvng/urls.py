from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.articles, name='articles'),
    path('article/<title>/', views.article_view, name='article'),
    path('about/', views.about, name='about'),
    path('search/', views.articles, name='search'),
]