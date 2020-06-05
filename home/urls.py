from django.urls import path
from . import views
from carts.views import cart
from carts.views import add_cart
from carts.views import remove_cart

app_name = 'home'
urlpatterns = [
    path('',views.homepage,name='homeurl'),
    path('cart',cart, name='cart'),
    path('cat',views.category_view,name = 'category'),
    path('cat/<slug>',views.categoryslug,name = 'categoryslug'),
    path('<slug>',views.product_detail,name='product_detail'),
    path('cart/<addslug>',add_cart,name='add_cart'),
    path('cart/r/<removeslug>',remove_cart,name='remove_cart'),

]
