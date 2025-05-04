from django.db import models
from django.conf import settings
from themes.models import Theme

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL única para el dashboard, ej: 'mi-dashboard'")
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.display_name} ({self.slug})"

    def get_absolute_url(self):
        return f"/{self.slug}/"