from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 10000)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

