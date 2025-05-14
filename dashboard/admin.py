from django.contrib import admin
from .models import Profile, Theme

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "slug", "user", "theme", "created_at")
    search_fields = ("display_name", "slug", "user__email")
    list_filter = ("theme", "created_at")

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name", "background_color", "text_color", "primary_color", "font_family", "background_image")
    search_fields = ("name",)
    list_filter = ("background_color", "text_color", "primary_color")

admin.site.register(Profile, ProfileAdmin)