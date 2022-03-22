from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Products.models import Supply, Suppliers, Production, Bid
from Products.serializers import SupplySerializer, SuppliersSerializer, ProductionSerializer, BidSerializer


class SuppliersApiTestCase(APITestCase):
    def test_suppliers_get(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7)
        url = reverse("suppliers-list")
        response = self.client.get(url)
        serializer_data = SuppliersSerializer([supplier_1, supplier_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class SupplyApiTestCase(APITestCase):
    def test_supply_get(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20, is_active=True)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7, is_active=False)
        supply_1 = Supply.objects.create(supplier=supplier_1, date="2022-02-10", amount="345.50")
        supply_2 = Supply.objects.create(supplier=supplier_2, date="2022-02-11", amount="234.30")
        url = reverse("supply-list")
        response = self.client.get(url)
        serializer_data = SupplySerializer([supply_1, supply_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class ProductionApiTestCase(APITestCase):
    def test_production_get(self):
        product_1 = Production.objects.create(name="CoffeeABE", size="250", price="50.00")
        product_2 = Production.objects.create(name="CoffeeAWE", size="1000", price="150.00")
        url = reverse("production-list")
        response = self.client.get(url)
        serializer_data = ProductionSerializer([product_1, product_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class BidApiTestCase(APITestCase):
    def test_bid_get(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20, is_active=True)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7, is_active=False)
        bid_1 = Bid.objects.create(supplier=supplier_1, text="milk 4, coffee 5")
        bid_2 = Bid.objects.create(supplier=supplier_2, text="woter 7, sirop 6")
        url = reverse("bid-list")
        response = self.client.get(url)
        serializer_data = BidSerializer([bid_1, bid_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
