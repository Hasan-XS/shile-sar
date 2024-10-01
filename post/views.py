from django.shortcuts import render
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

