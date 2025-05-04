from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserLink
from .forms import UserLinkForm

@login_required
def manage_links(request):
    links = UserLink.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('manage_links')
    else:
        form = UserLinkForm()

    return render(request, "profiles/manage_links.html", {
        'form': form,
        'links': links,
    })

@login_required
def delete_link(request, link_id):
    link = get_object_or_404(UserLink, id=link_id, user=request.user)
    link.delete()
    return redirect('manage_links')


@login_required
def edit_link(request, link_id):
    link = get_object_or_404(UserLink, id=link_id, user=request.user)

    if request.method == "POST":
        form = UserLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect("manage_links")
    else:
        form = UserLinkForm(instance=link)

    return render(request, "profiles/edit_link.html", {
        "form": form,
        "link": link
    })

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("manage_links")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profiles/edit_profile.html", {"form": form})

