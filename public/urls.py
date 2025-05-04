from django.urls import path
from . import views

urlpatterns = [
    path("@<str:username>", views.public_profile, name="public_profile"),
]
