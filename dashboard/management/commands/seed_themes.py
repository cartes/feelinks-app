from django.core.management.base import BaseCommand
from dashboard.models import Theme

class Command(BaseCommand):
    help = 'Crea temas predefinidos para perfiles'

    def handle(self, *args, **kwargs):
        themes = [
            {
                "name": "light",
                "background_color": "#ffffff",
                "text_color": "#000000",
                "primary_color": "#2563eb",
                "font_family": "sans"
            },
            {
                "name": "dark",
                "background_color": "#1f2937",
                "text_color": "#f9fafb",
                "primary_color": "#3b82f6",
                "font_family": "sans"
            },
            {
                "name": "neon",
                "background_color": "#0f0f0f",
                "text_color": "#39ff14",
                "primary_color": "#ff00ff",
                "font_family": "mono"
            }
        ]

        for data in themes:
            obj, created = Theme.objects.get_or_create(name=data["name"], defaults=data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Tema "{data["name"]}" creado.'))
            else:
                self.stdout.write(self.style.WARNING(f'Tema "{data["name"]}" ya existe.'))
