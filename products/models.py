from django.db import models


class Product(models.Model):
    name=models.CharField(unique=True)
    amount=models.IntegerField()
    price=models.FloatField()
