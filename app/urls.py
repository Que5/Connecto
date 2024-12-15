from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ArticleDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete"),
]