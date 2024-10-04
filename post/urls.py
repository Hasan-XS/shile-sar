from django.urls import path
from .views import index_view, posts_by_category, post_details_view

urlpatterns = [
    path("", index_view, name="index_home"),
    path(
        "posts/category/<str:category_name>/",
        posts_by_category,
        name="posts_by_category",
    ),
    path("posts/details/<pk>/", post_details_view, name="post_details"),
    
]
