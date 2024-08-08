from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart
from django.contrib import messages
from django.contrib.messages import get_messages

# Create your views here.
def index(request):

    products = Product.objects.all()

    return render(request, 'main/home.html', {'products': products})


def product(request, name):
    product = Product.objects.get(product_name=name)

    return render(request, 'main/product.html', {'product': product})


def addToCart(request, id):

    product = Product.objects.get(id=id)

    if Cart.objects.filter(product=product).exists():
        messages.info(request, "this item is already added in the cart")

        return redirect('/')
    
    else:
        add_product = Cart.objects.create(product=product, subtotal_price=product.price)
        add_product.save()
        
        messages.info(request, "your item has beed added to the cart")
        return redirect('/')

def remove(request, id):
    product = Cart.objects.get(id=id)

    product.delete()
    return redirect('shoppingCart')



def shoppingCart(request):

    products = Cart.objects.all()
    
    
    return render(request, 'main/shoppingCart.html', {'products':products})


def checkout(request):
    return render(request, 'main/checkout.html')