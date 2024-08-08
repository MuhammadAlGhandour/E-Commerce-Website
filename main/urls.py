from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:name>', views.product, name='product'),
    path('addToCart/<int:id>', views.addToCart, name='addToCart'),
    path('remove/<str:id>', views.remove, name='remove'),
    path('shoppingCart', views.shoppingCart, name='shoppingCart'),
    path('checkout', views.checkout, name='checkout')
]