from django.urls import path
from .views import ArticleCreateView, ArticleListView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete"),
]