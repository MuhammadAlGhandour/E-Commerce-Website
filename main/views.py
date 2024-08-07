from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()

    return render(request, 'main/home.html', {'products': products})


def product(request, name):
    product = Product.objects.get(product_name=name)
    return render(request, 'main/product.html', {'product': product})

product_list = []
def addToCart(request, id): # i want to get the specific product/s that the user selected

    product = Product.objects.get(id=id)
    product_list.append(product)
    return HttpResponse(product_list)

def shoppingCart(request):
    return render(request, 'main/shoppingCart.html')


def checkout(request):
    return render(request, 'main/checkout.html')