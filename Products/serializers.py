from rest_framework.serializers import ModelSerializer

from Products.models import Supply, Suppliers, Production, Bid


class SupplySerializer(ModelSerializer):
    class Meta:
        model = Supply
        fields = ["supplier", "date", "amount"]


class SuppliersSerializer(ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ["name", "payment_deferment", "is_active"]


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = Production
        fields = ["name", "size", "price"]


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = ["supplier", "text"]