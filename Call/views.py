from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def contact_profile(request):
    return render(request, "contact-profile.html")

def edit(request):
    return render(request, "edit.html")

def delete(request):
    return render(request, "delete.html")