from django.db import models

from products.models import Product

class Shop(models.Model):
    name = models.CharField(unique=True)
    products = models.ManyToManyField(Product)