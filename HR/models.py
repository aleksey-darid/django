from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateTimeField(null=True)
    date_to = models.DateTimeField(null=True)
    delta = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.date_from}: {self.date_to}: {self.delta}"
