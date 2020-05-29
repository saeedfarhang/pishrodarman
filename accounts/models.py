from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=12,blank=True,null=True)
    location = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.user.username
    