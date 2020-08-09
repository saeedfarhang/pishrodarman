from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def tickets(request):
    form = forms.ticketform()

    return render(request,'ticketing/tickets.html', {'form' : form})