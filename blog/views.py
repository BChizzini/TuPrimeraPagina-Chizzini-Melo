from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post
from .forms import PostForm, CategoryForm, AuthorForm


def post_list(request):
    posts = Post.objects.select_related("author", "category").all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = CategoryForm()
    return render(request, "blog/category_form.html", {"form": form})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog:post_list")
    else:
        form = AuthorForm()
    return render(request, "blog/author_form.html", {"form": form})


def search(request):
    query = request.GET.get("q", "").strip()
    results = []
    if query:
        results = (
            Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            .select_related("author", "category")
        )
    return render(request, "blog/search.html", {"query": query, "results": results})


