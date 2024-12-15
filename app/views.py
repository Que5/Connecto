from django.shortcuts import render
from .models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy 
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "app/home.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name = "app/article_create.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "app/article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = "__all__"
    template_name = "app/article_update.html"
    success_url = reverse_lazy("home")


class ArticleDeleteView(DetailView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")



