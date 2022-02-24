from django.db import models


class Suppliers(models.Model):
    name = models.CharField(max_length=200)
    payment_deferment = models.IntegerField(default=0)
    is_active = models.BooleanField(null=True)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.payment_deferment}: {self.is_active}"


class Production(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.size}: {self.price}"


class Supply(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.supplier}: {self.date}: {self.amount}"


class Bid(models.Model):
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"id {self.id}: {self.supplier}: {self.text}"
