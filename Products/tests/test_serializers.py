from django.test import TestCase

from Products.models import Supply, Suppliers, Production, Bid
from Products.serializers import SupplySerializer, SuppliersSerializer, ProductionSerializer, BidSerializer


class SuppliersSerializerTestCase(TestCase):
    def test_ok(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20, is_active=True)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7, is_active=False)
        data = SuppliersSerializer([supplier_1, supplier_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "name": "NOJACS",
                "payment_deferment": 20,
                "is_active": True

            },
            {
                # "id": user_2.id,
                "name": "FORNAX",
                "payment_deferment": 7,
                "is_active": False
            }
        ]
        self.assertEqual(expected_data, data)


class SupplySerializerTestCase(TestCase):
    def test_ok(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20, is_active=True)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7, is_active=False)
        supply_1 = Supply.objects.create(supplier=supplier_1, date="2022-02-10", amount="345.50")
        supply_2 = Supply.objects.create(supplier=supplier_2, date="2022-02-11", amount="234.30")
        data = SupplySerializer([supply_1, supply_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "supplier": 1,
                "date": "2022-02-10",
                "amount": "345.50"

            },
            {
                # "id": user_2.id,
                "supplier": 2,
                "date": "2022-02-11",
                "amount": "234.30"
            }
        ]
        self.assertEqual(expected_data, data)


class ProductionSerializerTestCase(TestCase):
    def test_ok(self):
        product_1 = Production.objects.create(name="CoffeeABE", size="250", price="50.00")
        product_2 = Production.objects.create(name="CoffeeAWE", size="1000", price="150.00")
        data = ProductionSerializer([product_1, product_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "name": "CoffeeABE",
                "size": "250",
                "price": "50.00"

            },
            {
                # "id": user_2.id,
                "name": "CoffeeAWE",
                "size": "1000",
                "price": "150.00"
            }
        ]
        self.assertEqual(expected_data, data)


class BidSerializerTestCase(TestCase):
    def test_ok(self):
        supplier_1 = Suppliers.objects.create(name="NOJACS", payment_deferment=20, is_active=True)
        supplier_2 = Suppliers.objects.create(name="FORNAX", payment_deferment=7, is_active=False)
        bid_1 = Bid.objects.create(supplier=supplier_1, text="milk 4, coffee 5")
        bid_2 = Bid.objects.create(supplier=supplier_2, text="woter 7, sirop 6")
        data = BidSerializer([bid_1, bid_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "supplier": 1,
                "text": "milk 4, coffee 5"
            },
            {
                # "id": user_2.id,
                "supplier": 2,
                "text": "woter 7, sirop 6"
            }
        ]
        self.assertEqual(expected_data, data)

