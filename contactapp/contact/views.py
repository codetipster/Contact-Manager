from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts':contacts})

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email =  request.POST['email'],
            phone_number = request.POST['phone_number'],
            address =  request.POST['address']
            
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')    