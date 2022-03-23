from rest_framework.serializers import ModelSerializer

from Products.models import Suppliers, Production, Bid, Supply


class SupplySerializer(ModelSerializer):
    class Meta:
        model = Supply
        fields = ["supplier", "date", "amount"]


class SuppliersSerializer(ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ["name", "payment_deferment"]


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = Production
        fields = ["name", "size", "price"]


class BidSerializer(ModelSerializer):
    class Meta:
        model = Bid
        fields = ["data", "text"]
