from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            'placeholder': 'Ej: name@email.com'
        }
    ))

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ej: nombredeusuario"
        }
    ))

    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Ej: $ad$22123$@"
        }
    ))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={
            "class": "w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Confirme su contraseña"
        }
    ))

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full rounded-lg border border-gray-300 px-4 py-2 text-sm',
        'placeholder': 'nombredeusuario'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full rounded-lg border border-gray-300 px-4 py-2 text-sm',
        'placeholder': 'contraseña'
    }))
