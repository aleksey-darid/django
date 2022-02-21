from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)


class Workers(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    rate_per_hour = models.IntegerField(default=0)


class Administration(models.Model):
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
