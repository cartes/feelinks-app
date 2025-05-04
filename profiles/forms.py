from django import forms
from .models import UserLink

class UserLinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['title', 'url', 'order']
        widgets = {
            "title": forms.TextInput(attrs={"class": "input"}),
            "url": forms.URLInput(attrs={"class": "input"}),
            "order": forms.NumberInput(attrs={"class": "input"}),
        }