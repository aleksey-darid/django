from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}: {self.email}"


class Workers(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    rate_per_hour = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}: {self.email}: {self.rate_per_hour}"


class Administration(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}: {self.email}"
