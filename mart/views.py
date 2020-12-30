from django.shortcuts import render

from .models import *

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'mart/home.html', context=context)