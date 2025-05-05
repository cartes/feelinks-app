from django.db import models
from django.conf import settings
from themes.models import Theme

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
    avatar_url = models.URLField(blank=True)
    theme = models.CharField(max_length=20, choices=[
        ("light", "Claro"),
        ("dark", "Oscuro"),
        ("neon", "Neón"),
        ("custom", "Personalizado")  # 👈 nuevo tipo
    ], default="light")

    primary_color = models.CharField(max_length=7, default="#2563EB")
    text_color = models.CharField(max_length=7, default="#000000")
    background_color = models.CharField(max_length=7, default="#FFFFFF")
    font_family = models.CharField(max_length=20, choices=FONT_CHOICES, default="sans")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.slug})"

    def get_absolute_url(self):
        return f"/{self.slug}/"