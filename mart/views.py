from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

from .models import *
from .decorators import vip_required, stock_is_enogh

User = get_user_model()

def home(request):
    products = Product.objects.all()
    users = User.objects.filter(is_superuser=False)
    context = {
        'products': products,
        'users': users,
        }
    return render(request, 'mart/home.html', context=context)


@require_http_methods(['POST'])
@vip_required
@stock_is_enogh
def create_order(request):
    user = get_object_or_404(User, id=request.POST.get('user'))
    product = get_object_or_404(Product, id=request.POST.get('product'))
    quantity = request.POST.get('quantity')
    print(user, product, quantity, product.price)
    return redirect(reverse('mart:home'))