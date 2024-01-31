from django.db import models


class Product(models.Model):
    name=models.CharField(unique=True, max_length=200)
    amount=models.IntegerField()
    price=models.FloatField()
