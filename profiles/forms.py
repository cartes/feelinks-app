from django import forms
from .models import UserLink
from dashboard.models import Profile


class UserLinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['title', 'url', 'order']
        widgets = {
            "title": forms.TextInput(attrs={"class": "input"}),
            "url": forms.URLInput(attrs={"class": "input"}),
            "order": forms.NumberInput(attrs={"class": "input"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "display_name", "bio", "avatar", "theme",
            "background_color", "text_color", "primary_color",
            "font_family"
        ]

        widgets = {
            "display_name": forms.TextInput(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Ej: Cristian"
            }),
            "bio": forms.Textarea(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                "rows": 3,
                "placeholder": "Cuéntanos un poco sobre ti..."
            }),
            "avatar": forms.ClearableFileInput(attrs={
                "class": "w-full block text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            }),
            "theme": forms.Select(attrs={
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
            "font_family": forms.Select(attrs={
                "id": "id_font_family",
                "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            }),
            "primary_color": forms.TextInput(attrs={
                "type": "color",
                "class": "w-full h-10 rounded-md border border-gray-300 cursor-pointer"
            }),
            "text_color": forms.TextInput(attrs={
                "type": "color",
                "class": "w-full h-10 rounded-md border border-gray-300 cursor-pointer"
            }),
            "background_color": forms.TextInput(attrs={
                "type": "color",
                "class": "w-full h-10 rounded-md border border-gray-300 cursor-pointer"
            }),
        }

        def clean(self):
            cleaned_data = super().clean()
            theme = cleaned_data.get("theme")

            # Reemplaza valores si se seleccionó un tema fijo
            if theme == "light":
                cleaned_data["background_color"] = "#ffffff"
                cleaned_data["text_color"] = "#000000"
                cleaned_data["primary_color"] = "#2563eb"
            elif theme == "dark":
                cleaned_data["background_color"] = "#1f2937"
                cleaned_data["text_color"] = "#f9fafb"
                cleaned_data["primary_color"] = "#3b82f6"

            return cleaned_data
