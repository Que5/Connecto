from django.shortcuts import render
from .models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "app/home.html"


class ArticleCreateView(CreateView, LoginRequiredMixin):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    template_name = "app/article_create.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView, LoginRequiredMixin):
    model = Article
    template_name = "app/article_detail.html"


class ArticleUpdateView(UpdateView, LoginRequiredMixin):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_update.html"
    success_url = reverse_lazy("home")


class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")



