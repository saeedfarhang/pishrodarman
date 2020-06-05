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
        args = {'products':products,'x':x ,'lastProduct':last_products, 'category':category,'cartitems':cart_items } 
    else:
        args = {'products':products,'x':x ,'lastProduct':last_products, 'category':category}

    return render(request,'home/homepage.html',args)


def product_detail(request, slug):
    product = models.Product.objects.get(slug=slug)
    # return HttpResponse(english_name)
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(id = request.user.id)

        except Cart.DoesNotExist:
            new_cart = Cart(id = request.user.id)
            new_cart.save()

        cart = Cart.objects.get(id = request.user.id)
        cart_items = cart.products.all()
        args = {'product':product ,'cartitems':cart_items }
    else:
        args = {'product':product}

    return render(request,'home/product_detail.html',args)



def category_view(request):
    category = models.products_category.objects.all()
    template = 'home/category.html'
    context = {'category':category}
    return render(request,template,context)

def categoryslug(request,slug):
    cat = models.products_category.objects.get(slug=slug)
    product = models.Product.objects.filter(category = cat)
    

    template = 'home/cat_item.html'
    context = {'cat':cat,'product':product}
    return render(request,template,context)