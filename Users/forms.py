from django import forms

from Users.models import Workers


class WorkersForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ["rate_per_hour"]
