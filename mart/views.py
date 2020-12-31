from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import *
from .decorators import vip_required, stock_is_enogh

def home(request):
    products = Product.objects.all()
    customers = Customer.objects.filter()
    orders = Order.objects.all()
    context = {
        'products': products,
        'customers': customers,
        'orders': orders,
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

@require_http_methods(['POST'])
def delete_order(request):
    order = get_object_or_404(Order, id=request.POST.get('order'))
    if order.product.stock_pcs == 0:
        messages.info(request, f'Product ID {order.product.id} was replenished.')
    order.delete()
    return redirect(reverse('mart:home'))