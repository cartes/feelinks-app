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
            "display_name": forms.TextInput(attrs={"class": "form-input w-full"}),
            "bio": forms.Textarea(attrs={"class": "form-input w-full", "rows": 3}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-input w-full"}),
            "theme": forms.Select(attrs={"class": "form-select w-full"}),
            "font_family": forms.Select(attrs={"id": "id_font_family", "class": "form-select w-full"}),
            "primary_color": forms.TextInput(attrs={"type": "color", "class": "form-input w-full"}),
            "text_color": forms.TextInput(attrs={"type": "color", "class": "form-input w-full"}),
            "background_color": forms.TextInput(attrs={"type": "color", "class": "form-input w-full"}),
        }
