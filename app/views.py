from typing import Any

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from .models import Article
from django.db.models.query import QuerySet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "app/home.html"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        search = self.request.GET.get("search")
        queryset = super().get_queryset().filter(creator=self.request.user)
        if search:
            queryset = queryset.filter(title__search=search)
        return queryset.order_by("-created_at")
     


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
    
    def post(self, request:HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        messages.success(request, "Article deleted successfully.", extra_tags="destructive") 
        return super().post(request, *args, **kwargs)



