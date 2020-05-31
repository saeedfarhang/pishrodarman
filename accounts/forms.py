from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,label='نام کاربری*')
    password1 = forms.CharField(max_length=30, required=True,label='رمز عبور*',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, required=True,label='تایید رمز عبور*',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "password1","password2"]
  


class UserProfileForm(forms.ModelForm):
    phoneNumber = forms.CharField(label='شماره تماس' ,max_length=12, required=False,widget=forms.NumberInput())
    location = forms.CharField(label='آدرس', max_length=100, required=False)
    email = forms.EmailField(label='ایمیل', required=False)
    fullname = forms.CharField(max_length=30,label='نام و نام خانوادگی', required=False)


    class Meta:
        model = UserProfile
        fields = ["phoneNumber","location","fullname" , "email"]
