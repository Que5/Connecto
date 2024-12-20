import re

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from app.managers import UserProfileManager

# Create your models here.

ARTICLE_STATUS = (
        ("draft", "Draft"),
        ("in progress", "In progress"), 
        ("published", "Published"),
    )

class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)

    objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Article(models.Model):                                                               
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default="")
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20, 
                                choices=ARTICLE_STATUS,
                                default="draft"
                            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>","", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)
