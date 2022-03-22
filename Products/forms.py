from django import forms
from .models import Production, Supply, Suppliers, Bid


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ["name", "size", "price"]


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["supplier", "date", "amount"]
        widgets = {"date": forms.SelectDateWidget}


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ["name", "payment_deferment"]


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ["text"]
