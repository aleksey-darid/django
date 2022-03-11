from django.db import models


"""class Users(models.Model):
    name = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=254, blank=False)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}"


class Workers(models.Model):
    name = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=254, blank=False)
    rate_per_hour = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}: {self.rate_per_hour}"


class Administration(models.Model):
    name = models.CharField(max_length=254, blank=False)
    password = models.CharField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"id {self.id}: {self.name}: {self.password}: {self.phone_number}: {self.email}" """
