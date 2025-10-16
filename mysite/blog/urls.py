from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/category/<int:category_id>/', views.article_category_list, name='article_category_list'),
path('articles/<slug:post_slug>/', views.article_detail, name='article_detail'),
]

