from django.urls import path
from . import views
from profiles.views import upload_avatar

urlpatterns = [
    path("", views.dashboard_home, name="dashboard_home"),
    path('manage_links/', views.manage_links, name='manage_links'),
    path('delete_link/<int:link_id>/', views.delete_link, name='delete_link'),
    path("editar-enlace/<int:link_id>/", views.edit_link, name="edit_link"),
    path("editar-perfil/", views.edit_profile, name="edit_profile"),
    path('preview/', views.preview_profile, name='preview_profile'),
    path("upload-avatar/", upload_avatar, name="upload_avatar"),
]
