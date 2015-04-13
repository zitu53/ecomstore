from django.shortcuts import render

from cart import cart
# Create your views here.
def show_cart(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return render(request, "cart/cart.html", locals())