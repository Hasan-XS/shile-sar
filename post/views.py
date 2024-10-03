from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.


def index_view(request):
    posts = list(reversed(Post.objects.all()))
    return render(
        request,
        "index.html",
        {
            "posts": posts,
        },
    )


def posts_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    posts = list(reversed(Post.objects.filter(category=category)))

    return render(
        request,
        "post/posts_by_category.html",
        {
            "posts": posts,
            "category": category,
        },
    )
