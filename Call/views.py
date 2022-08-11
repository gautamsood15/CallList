from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, "index.html", context)


def profile(request):
    return render(request, "contact-profile.html")

def edit(request):
    return render(request, "edit.html")

def delete(request):
    return render(request, "delete.html")

def new(request):
    if request.method == "POST":
        new_contact = Contact.objects.create(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('/')    
    return render(request, "new.html")