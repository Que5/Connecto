from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "word_count", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["title", "content"]
    date_hierarchy = "created_at"
    ordering =["created_at"]
    readonly_fields = ["word_count", "created_at", "updated_at"]


admin.site.register(UserProfile)
admin.site.register(Article, ArticleAdmin)
