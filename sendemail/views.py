from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from datetime import datetime
from sendemail.models import Contact


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if (request.method == 'POST'):
            name = request.POST.get('name')
            from_email = request.POST.get('from_email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            try:
                contact = Contact(name=name, from_email=from_email,
                                  subject=subject, message=message,
                                  date=datetime.today())
                contact.save()
            except BadHeaderError:
                return HttpResponse('Ugyldig rute')
            return redirect('success')
    return render(request, 'contact.html', {'form': form})


def successView(request):
    return render(request, 'success.html')
