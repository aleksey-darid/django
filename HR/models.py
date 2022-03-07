from django.db import models
from Users.models import Workers


class Schedule(models.Model):
    data = models.DateField()
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
    hours_from = models.DecimalField(max_digits=4, decimal_places=2)
    hours_until = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"id {self.id}: {self.data}: {self.worker.name}: {self.hours_from}: {self.hours_until}"
