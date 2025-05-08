from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import SignUpForm, PasswordResetCustomForm, SetPasswordCustomForm, CustomLoginForm

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'public/login.html'  # o el path correcto de tu plantilla
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse('dashboard_home')

def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    links = user.links.all()

    return render(request, "public/profile.html", {
        "profile_user": user,
        "links": links,
    })


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_home')
    else:
        form = SignUpForm()

    return render(request, 'public/signup.html', {'form': form})


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetCustomForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='public/password_reset_email.html',
                html_email_template_name='public/password_reset_email.html',
            )
            return render(request, 'public/password_reset_done.html')
    else:
        form = PasswordResetCustomForm()

    return render(request, 'public/password_reset.html', {'form': form})

def reset_confirm(request):
    if request.method == 'POST':
        form = SetPasswordCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SetPasswordCustomForm()

    return render(request, 'public/password_reset_confirm.html', {'form': form})

