from django.contrib import admin
from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name='blog-index'),
    path('article_<str:article_id>/', article, name='blog-article'),
    
]