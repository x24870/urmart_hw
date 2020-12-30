from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Product

User = get_user_model()

def vip_required(func):
    def decorator(*args, **kwargs):
        request = args[0]
        product = get_object_or_404(Product, id=request.POST.get('product'))
        user = get_object_or_404(User, id=request.POST.get('user'))
        if product.vip_only and not user.vip:
            messages.error(request ,"This product only available for VIP members!")
            return redirect(reverse('mart:home'))
        return func(*args, **kwargs)
    return decorator

def stock_is_enogh(func):
    def decorator(*args, **kwargs):
        request = args[0]
        product = get_object_or_404(Product, id=request.POST.get('product'))
        quantity = int(request.POST.get('quantity'))
        if product.stock_pcs < quantity:
            messages.error(request ,"Sorry, the stock of this product is not enough!")
            return redirect(reverse('mart:home'))
        return func(*args, **kwargs)
    return decorator