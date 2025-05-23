from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import UserLink
from dashboard.models import Theme
from .forms import UserLinkForm, ProfileForm

from django.core.serializers.json import DjangoJSONEncoder
import json

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
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("edit_profile")  # pon el nombre correcto de tu URL aquí
    else:
        form = ProfileForm(instance=profile)

    themes = list(Theme.objects.all().values(
        'id', 'name', 'background_color', 'text_color', 'primary_color'
    ))

    context = {
        "form": form,
        "profile": profile,
        "themes_json": json.dumps(themes, cls=DjangoJSONEncoder),
    }

    return render(request, "profiles/edit_profile.html", context)


@login_required
def preview_profile(request):
    username = request.user.username
    public_url = f"/@{username}"
    return render(request, "profiles/preview_profile.html", {"public_url": public_url})


@login_required
def dashboard_home(request):
    return render(request, "profiles/dashboard_home.html")


@login_required
@require_POST
def upload_avatar(request):
    avatar = request.FILES.get("avatar")

    if avatar:
        profile = request.user.profile
        profile.avatar = avatar
        profile.save()
        return JsonResponse({"success": True, "avatar_url": profile.avatar.url})
    else:
        return JsonResponse({"success": False, "error": "No se envió ninguna imagen."}, status=400)

@login_required
@require_POST
def reorder_links(request):
    try:
        data = json.loads(request.body)
        ordered_ids = data.get('ordered_ids', [])

        for index, link_id in enumerate(ordered_ids):
            UserLink.objects.filter(id=link_id, user=request.user).update(order=index)

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
