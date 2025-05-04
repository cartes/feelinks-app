from django.contrib import admin
from .models import Theme

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_free", "background_class", "text_class", "button_class", "created_at")
    search_fields = ("name",)
    list_filter = ("is_free",)
