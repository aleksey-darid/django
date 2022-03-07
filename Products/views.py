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
    if request.method == "GET":
        dat = Suppliers.objects.in_bulk()
        print(dat)
        suppliers_list = {"suppliers_list": str(dat)}
        return render(request, "suppliers_app.html", context=suppliers_list)

    elif request.method == "POST":
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}
        message = {"message": "Поставщик добавлен."}
        data = request.POST.get
        print(data)
        name = data("name")
        print(name)
        pay_def = data("pay_def")
        print(pay_def)

        count_name = 0
        for _ in name:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "suppliers_app.html", context=error_message_empty)

        count_name = 0
        for _ in pay_def:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "suppliers_app.html", context=error_message_empty)

        new_supplier = Suppliers.objects.create(name=f"{name}", payment_deferment=f"{pay_def}")
        new_supplier.save()
        return render(request, "suppliers_app.html", context=message)


def production_app(request):
    return render(request, "production_app.html")


def bid_app(request):
    return render(request, "bid_app.html")
