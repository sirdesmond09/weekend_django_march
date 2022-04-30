from django.urls import path
from . import views


urlpatterns = [
    path("blog_posts/", views.posts),
    path("blog_posts/<int:post_id>", views.post_detail)
]
