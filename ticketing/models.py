from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class ticket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1500)
