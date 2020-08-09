from django import forms
from .models import ticket

class ticketform(forms.ModelForm):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=1500)
    class Meta:
        model = ticket
        fields = ['subject' , 'message']