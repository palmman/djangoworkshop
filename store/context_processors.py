from store.models import Category, Cart, CartItem
from .views import *

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id=cart_id(request))
            cart_item = CartItem.objects.all().filter(cart=cart[:1])
            for item in cart_item:
                item_count += item.quantity

        except Cart.DoesNotExist :
            item_count = 0
    return dict(item_count=item_count)