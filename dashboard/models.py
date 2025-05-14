import os
from django.db import models
from django.conf import settings
from themes.models import Theme
from django.core.validators import FileExtensionValidator
from datetime import datetime


def upload_avatar_to(instance, filename):
    user_id = instance.user.id
    fecha = datetime.now().strftime("%Y%m%d")
    extension = os.path.splitext(filename)[1]

    return f"avatars/id-{user_id}-{fecha}/{filename}{extension}"


class Profile(models.Model):
    FONT_CHOICES = [
        ("sans", "Sans (por defecto)"),
        ("serif", "Serif"),
        ("mono", "Monoespaciada"),
        ("inter", "Inter"),
        ("poppins", "Poppins"),
        ("raleway", "Raleway"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL única para el dashboard, ej: 'mi-dashboard'")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to=upload_avatar_to,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])],
        blank=True,
        null=True
    )

    theme = models.CharField(max_length=20, choices=[
        ("light", "Claro"),
        ("dark", "Oscuro"),
        ("neon", "Neón"),
        ("custom", "Personalizado")  # 👈 nuevo tipo
    ], default="light")

    background_image = models.ImageField(
        upload_to="profile_backgrounds/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])]
    )

    primary_color = models.CharField(max_length=7, default="#2563EB")
    text_color = models.CharField(max_length=7, default="#000000")
    background_color = models.CharField(max_length=7, default="#FFFFFF")
    font_family = models.CharField(max_length=20, choices=FONT_CHOICES, default="sans")
    show_invite_footer = models.BooleanField(default=True)
    enable_animations = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.slug})"

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Theme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    background_color = models.CharField(max_length=7, default="#ffffff")
    text_color = models.CharField(max_length=7, default="#000000")
    primary_color = models.CharField(max_length=7, default="#2563eb")

    FONT_CHOICES = [
        ("sans", "Sans (por defecto)"),
        ("serif", "Serif"),
        ("mono", "Monoespaciada"),
        ("inter", "Inter"),
        ("poppins", "Poppins"),
        ("raleway", "Raleway"),
    ]

    font_family = models.CharField(max_length=50, choices=FONT_CHOICES, default="sans")
    background_image = models.ImageField(
        upload_to="theme_backgrounds/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"])]
    )

    def __str__(self):
        return self.name
