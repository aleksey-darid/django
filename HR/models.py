from django.db import models
from django.contrib.auth.models import User

from Users.models import Workers


class Schedule(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    delta = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.date}: {self.time_from}: {self.time_to}: {self.delta}"


class Wages(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField(null=True)
    date_to = models.DateField(null=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    total_wages = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.worker}: {self.date_from}: {self.date_to}: {self.hours}: {self.total_wages}"
