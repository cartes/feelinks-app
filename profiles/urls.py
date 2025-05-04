from django.urls import path
from . import views

urlpatterns = [
    path('manage_links/', views.manage_links, name='manage_links'),
    path('delete_link/<int:link_id>/', views.delete_link, name='delete_link'),
]