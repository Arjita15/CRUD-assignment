from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("note/<int:id>/", views.read_one, name="read_one"),
    path("note/<int:id>/edit/", views.update_one, name="update_one"),
    path("note/<int:id>/delete/", views.delete_one, name="delete_one"),
]