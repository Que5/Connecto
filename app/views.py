from django.shortcuts import render
from .models import Article
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy 
# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name = "app/article_create.html"

class ArticleListView(ListView):
    model = Article
    template_name = "app/article_list.html"



