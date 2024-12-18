from django.shortcuts import render
from .models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "app/home.html"

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Article.objects.filter(creator=self.request.user).order_by("-created_at")
    #     else:
    #         return Article.objects.none()


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("home")
    template_name = "app/article_create.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "app/article_detail.html"


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    template_name = "app/article_update.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user == self.get_object().creator


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user == self.get_object().creator



