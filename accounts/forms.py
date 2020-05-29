from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields = ["username","first_name" ,'last_name', "email", "password1","password2"]

class UserProfileForm(forms.ModelForm):
    phoneNumber = forms.CharField(label='شماره تماس' ,max_length=12, required=False,
    widget=forms.NumberInput()
    )
    class Meta:
        model = UserProfile
        fields = ("phoneNumber","location")