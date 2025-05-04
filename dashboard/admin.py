from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "slug", "user", "theme", "created_at")
    search_fields = ("display_name", "slug", "user__email")
    list_filter = ("theme", "created_at")

admin.site.register(Profile, ProfileAdmin)