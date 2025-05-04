from django.urls import path
from . import views

urlpatterns = [
    path('manage_links/', views.manage_links, name='manage_links'),
    path('delete_link/<int:link_id>/', views.delete_link, name='delete_link'),
    path("editar-enlace/<int:link_id>/", views.edit_link, name="edit_link"),
    path("editar-perfil/", views.edit_profile, name="edit_profile"),
]
