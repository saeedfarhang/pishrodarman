from django.shortcuts import render, redirect, HttpResponse
from . import forms
from . import models
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
            form = forms.RegisterForm(request.POST)
            form1 = forms.UserProfileForm(request.POST)
            if form.is_valid() and form1.is_valid():
                user = form.save()
                profile = form1.save(commit=False)
                profile.user = user
                profile.save()
                new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
                
                login(request,new_user)
                return redirect("/")
    else:
        form = forms.RegisterForm()
        form1 = forms.UserProfileForm()

    return render(request,'accounts/user_signup.html',{"form":form,"form1":form1 })



@login_required(login_url = 'accounts/login')
def profile(request):
    profile = models.UserProfile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def logout_view(request):
    logout(request)
    return render(request,'accounts/logout.html')


def update_profile(request):
    profile = models.UserProfile.objects.get(user=request.user)


    if request.method == "POST":
        form1 = forms.UserProfileForm(request.POST , instance=profile)


        if form1.is_valid():

            update1 = form1.save(commit=False)
            update1.user = request.user
            update1.save()
            return redirect("/")
    
    else:
        form1 = forms.UserProfileForm(instance=profile)



    return render(request,'accounts/update_profile.html',{'form1':form1})