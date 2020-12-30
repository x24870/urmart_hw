from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import *
from .decorators import vip_required, stock_is_enogh

def home(request):
    products = Product.objects.all()
    customers = Customer.objects.filter()
    context = {
        'products': products,
        'customers': customers,
        }
    return render(request, 'mart/home.html', context=context)


@require_http_methods(['POST'])
@vip_required
@stock_is_enogh
def create_order(request):
    customer = get_object_or_404(Customer, id=request.POST.get('customer'))
    product = get_object_or_404(Product, id=request.POST.get('product'))
    quantity = request.POST.get('quantity')
    # print(customers, product, quantity, product.price)
    order = Order.objects.create_order(
        customer=customer,
        product=product,
        quantity=quantity
        )
    return redirect(reverse('mart:home'))