from django.shortcuts import render,HttpResponse
from . import models
from carts.models import Cart
# Create your views here.
def homepage(request):
    products = models.Product.objects.all().order_by('-date')
    category = models.products_category.objects.all()
    last_products = models.Product.objects.all().order_by('-date')[:5]
    x = 'aaa'

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(id = request.user.id)

        except Cart.DoesNotExist:
            new_cart = Cart(id = request.user.id)
            new_cart.save()

        cart = Cart.objects.get(id = request.user.id)
        cart_items = cart.products.all()
        print(cart_items)
        args = {'products':products,'x':x ,'lastProduct':last_products, 'category':category,'cartitems':cart_items} 
    else:
        args = {'products':products,'x':x ,'lastProduct':last_products, 'category':category}

    return render(request,'home/homepage.html',args)


def product_detail(request, slug):
    product = models.Product.objects.get(slug=slug)
    # return HttpResponse(english_name)

    return render(request,'home/product_detail.html',{'product':product})


