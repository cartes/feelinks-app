from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, login
from .forms import SignUpForm

User = get_user_model()


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
