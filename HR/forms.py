from django import forms
from .models import Schedule, Wages


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ["date", "time_from", "time_to"]


class WagesForm(forms.ModelForm):
    class Meta:
        model = Wages
        fields = ["worker", "date_from", "date_to"]
        widgets = {"date_from": forms.SelectDateWidget,
                   "date_to": forms.SelectDateWidget}
