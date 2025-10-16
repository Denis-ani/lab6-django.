from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    return render(request, 'index.html')

def article_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'article_list.html', {'posts': posts})

def article_category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'article_category_list.html', {'category': category, 'posts': posts})

def article_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'article_detail.html', {'post': post})


