from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time_from = models.TimeField(null=True)
    time_to = models.TimeField(null=True)
    delta = models.IntegerField(default=0)

    def __str__(self):
        return f"id {self.id}: {self.date}: {self.time_from}: {self.time_to}: {self.delta}"
