from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()

    return render(request, 'main/home.html', {'products': products})


def product(request, name):
    product = Product.objects.get(product_name=name)
    return render(request, 'main/product.html', {'product': product})


def shoppingCart(request):
    return render(request, 'main/shoppingCart.html')


def checkout(request):
    return render(request, 'main/checkout.html')