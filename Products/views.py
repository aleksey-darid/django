from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Supply, Suppliers, Production, Bid
from .serializers import SupplySerializer, SuppliersSerializer, ProductionSerializer, BidSerializer


class SupplyView(ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class SuppliersView(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer


class ProductionView(ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class BidView(ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


def supply_app(request):
    return render(request, "supply_app.html")


def suppliers_app(request):
    return render(request, "suppliers_app.html")


def production_app(request):
    return render(request, "production_app.html")


def bid_app(request):
    return render(request, "bid_app.html")