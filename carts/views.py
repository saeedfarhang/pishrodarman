from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from . import models
from home.models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url = "accounts:login")
def cart(request):
    # if models.Cart.objects.get(id = request.user.id):
    #     pass
    # else:
    #     new_cart = models.Cart(id = request.user.id)
    #     new_cart.save()
    try:
        cart = models.Cart.objects.get(id = request.user.id)
    except models.Cart.DoesNotExist:
        pass
    
    cart = models.Cart.objects.get(id = request.user.id)

    context = {'cart':cart}

    return render(request,'carts/cart.html',context)


def add_cart(request, addslug):
    if request.user.is_authenticated:
        cart = models.Cart.objects.get(id = request.user.id)
        product = models.Product.objects.get(slug = addslug)
        exist = False
        if not product in cart.products.all():
            cart.products.add(product)
            
        else:
            exist = True
            print(exist)
            
        
    else:
        pass
    
    new_total = 0
    for item in cart.products.all():
        new_total += item.price

    

    return redirect(reverse('home:homeurl'))
        

def remove_cart(request , removeslug):
    if request.user.is_authenticated:
        cart = models.Cart.objects.get(id = request.user.id)
        product = models.Product.objects.get(slug = removeslug)
        cart.products.remove(product)
    return redirect("/")
