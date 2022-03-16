from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["date", "time_from", "time_to"]


