from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.contact_profile, name="contact-profile"),
    path("edit", views.edit, name="edit")
]