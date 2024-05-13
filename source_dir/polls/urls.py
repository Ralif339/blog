from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("posts", views.posts_list, name="list"),
    path("<slug:slug>", views.post_page, name="page"),
]
