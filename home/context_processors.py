from carts.models import Cart

def carttotal(request):
    # try:
    #     cart = Cart.objects.get(id = request.user.id)
    # except Cart.DoesNotExist:
    #     new_cart =Cart(id = request.user.id)
    #     new_cart.save()
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(id = request.user.id)
            context = {'items_total': cart.products.all().count()}
        except:
            context = {}
        
    else:
        context = {}
    return context