from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 10000)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    subtotal_price = models.IntegerField(default=0)

    def subtotal(self):
        self.subtotal_price = self.quantity * self.product.price

    def __str__(self):
        return self.product.product_name
