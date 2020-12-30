from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

from .models import *

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
def create_order(request):
    print(request.POST)
    return redirect(reverse('mart:home'))