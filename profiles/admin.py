from django.contrib import admin
from .models import UserLink

@admin.register(UserLink)
class UserLinkAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "url", "order", "created_at"]
    list_filter = ["user"]
    search_fields = ["title", "url"]
    ordering = ["order", "created_at"]