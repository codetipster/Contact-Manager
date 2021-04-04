from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''    
    return render(request, 'index.html', {'contacts':contacts, 'search_input': search_input})

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


def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contactsProfile.html', {'contact': contact})


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.full_name = request.POST['relationship']
        contact.full_name = request.POST['email']
        contact.full_name = request.POST['address']
        contact.full_name = request.POST['phone-number']

        contact.save()

        return redirect('/profile'+ str(contact.id))
    return render(request, 'editPage.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})    