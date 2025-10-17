from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("posts/nuevo/", views.post_create, name="post_create"),
    path("categorias/nueva/", views.category_create, name="category_create"),
    path("autores/nuevo/", views.author_create, name="author_create"),
    path("buscar/", views.search, name="search"),
]
