from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    links = user.links.all()

    return render(request, "public/profile.html", {
        "profile_user": user,
        "links": links,
    })
