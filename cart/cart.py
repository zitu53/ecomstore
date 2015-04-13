from cart.models import CartItem
from catalog.models import Product
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

import decimal
import random

CART_ID_SESSION_KEY = 'cart_id'

# get current users cart id
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

# generate a new random cart id
def _generate_cart_id():
    cart_id = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0,len(characters)-1)]
    return cart_id


def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):
    postdata = request.POST.copy()
    # get product slug from post data, blank if empty
    product_slug = postdata.get('product_slug','')
    # get quantity, return 1 if empty
    quantity = postdata.get('quantity',1)
    # fetch product or report missing page error
    p = get_object_or_404(Product, slug = product_slug)
    cart_products = get_cart_items(request)
    product_in_cart = False
    # check if product already in cart
    for cart_item in cart_products:
        if cart_item.product.id == p.id:
            # update quantity
            cart_item.augment_quantity(quantity)
            product_in_cart = True

    if not product_in_cart:
        # create and save new cart item
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.save()

def cart_distinct_item_count(request):
    return get_cart_items(request).count()

def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id = _cart_id(request))

# update quantity
def update_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        if (int)(quantity) > 0:
            cart_item.quantity = (int)(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        cart_item.delete()

def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for item in cart_products:
        cart_total += item.product.price * item.quantity
    return cart_total