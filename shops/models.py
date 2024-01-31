from django.db import models

from products.models import Product

class Shop(models.Model):
    name = models.CharField(unique=True, max_length=200)
    products = models.ManyToManyField(Product)