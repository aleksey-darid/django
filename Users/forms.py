from django import forms
from .models import Workers


class LoginForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ["name", "password"]
