from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects.all()

    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts=Contact.objects.all()
        search_input = ''
    context = {'contacts': contacts, 'search_input': search_input}
    return render(request, "index.html", context)


def profile(request, pk):

    contacts = Contact.objects.get(id=pk)
    context = {'contacts': contacts}
    return render(request, "contact-profile.html", context)

def edit(request, pk):

    contact = Contact.objects.get(id=pk)

    if request.method == "POST":
        info = request.POST

        contact.full_name = info['fullname']
        contact.relationship = info['relationship']
        contact.phone_number = info['phone']
        contact.email = info['email']
        contact.address = info['address']
        contact.save()

        
        return redirect('profile', pk=pk)




    context = {'contact': contact}
    return render(request, "edit.html", context)

def delete(request, pk):

    contact = Contact.objects.get(id=pk)

    if request.method == "POST":
        contact.delete()
        return redirect('index')


    context = {'contact': contact}
    return render(request, "delete.html", context)

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