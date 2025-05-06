from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from public import views as public_views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path("@<str:username>", views.public_profile, name="public_profile"),
    path('signup/', public_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='public/login.html',
        authentication_form=CustomLoginForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
