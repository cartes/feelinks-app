from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'plan', 'is_staff', 'is_active')

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Custom Fields", {
            "fields": ("plan",),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "first_name", "last_name", "plan", "password1", "password2"),
        }),
    )