from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from public import views as public_views
from .forms import CustomLoginForm
from .views import reset_password, CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path("@<str:username>", views.public_profile, name="public_profile"),
    path('signup/', public_views.signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('password_reset/', reset_password, name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='public/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='public/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='public/password_reset_complete.html'),
         name='password_reset_complete'),

]
