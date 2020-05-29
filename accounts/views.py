from django.shortcuts import render, redirect, HttpResponse
from . import forms
from . import models
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
            form = forms.RegisterForm(request.POST)
            profile_form = forms.UserProfileForm(request.POST)
            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile = profile_form.save(commit=False)
                profile.user = user

                profile.save()
                new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
                
                login(request,new_user)
                return redirect("/")
    else:
        form = forms.RegisterForm()
        profile_form = forms.UserProfileForm(request.POST)

    return render(request,'accounts/user_signup.html',{"form":form})



@login_required(login_url = 'accounts/login')
def profile(request):
    return render(request,'accounts/profile.html')

def logout_view(request):
    logout(request)
    return render(request,'accounts/logout.html')


def update_profile(request):
    profile = models.UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = forms.UserProfileForm(request.POST , instance=profile)

        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect("/")
    
    else:
        form = forms.UserProfileForm(instance=profile)

    return render(request,'accounts/update_profile.html',{'form':form})