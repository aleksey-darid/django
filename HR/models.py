from django.db import models
from Users.models import Workers


class Schedule(models.Model):
    data = models.DateField()
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=3, decimal_places=1)
