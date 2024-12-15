from django.urls import path
from .views import ArticleCreateView, ArticleListView

urlpatterns = [
    path("", ArticleListView.as_view(), name="home"),
    path("create/", ArticleCreateView.as_view(), name="create"),

]