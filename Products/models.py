from django.db import models


class Suppliers(models.Model):
    name = models.CharField(max_length=200)
    payment_deferment = models.IntegerField(default=0)
    is_active = models.BooleanField(null=True)


class Production(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Supply(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Bid(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
