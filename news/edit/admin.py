from django.contrib import admin
from .models import Category, News, Comment

admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "updated_at")
    list_display_links = ("title",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display = ("name", "email", "status", "created_at")
    list_display_links = ("name",)
    list_filter = ("status",)
    search_fields = ("name", "email", "content")
admin.site.register(Comment, AdminComment)
