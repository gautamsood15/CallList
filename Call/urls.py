from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("edit", views.edit, name="edit"),
    path("delete", views.delete, name="delete"),
    path("new", views.new, name="new")
]