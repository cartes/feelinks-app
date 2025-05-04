from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=200)
    is_free = models.BooleanField(default=True)

    background_class = models.CharField(max_length=200, help_text="ej: bg-white or bg-gradient-to-r from-purple-400 to-pink-500")
    text_class = models.CharField(max_length=200, help_text="ej: text-gray-900 or text-white")
    button_class= models.CharField(max_length=200, help_text="ej: bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Free' if self.is_free else 'Pro'})"