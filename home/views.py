from django.shortcuts import render
from . import models
# Create your views here.
def homepage(request):
    products = models.Products.objects.all()

    x = 'aaa'
    args = {'products':products,'x':x }
    return render(request,'home/homepage.html',args)
