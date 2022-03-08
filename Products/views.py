import datetime

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Suppliers, Production, Bid, Supply
from .serializers import SuppliersSerializer, ProductionSerializer, BidSerializer, SupplySerializer


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
    if request.method == "GET":
        dat = Supply.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 4:
                new_dat.append(i)
            elif count == 6:
                new_dat.append(i)
            elif count == 7:
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        list1 = {"list1": new_dat2}
        supply_list = {"supply_list": new_dat2}
        return render(request, "supply_app.html", context=supply_list)
    elif request.method == "POST":
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми. Либо нет такого поставщика"}
        message = {"message": "Поставка добавлена."}
        data = request.POST.get
        print(data)
        name = data("name")
        print(name)
        pay_sup = data("pay_sup")
        print(pay_sup)
        date = data("date")
        print(date)

        count_name = 0
        for _ in name:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "supply_app.html", context=error_message_empty)

        count_name = 0
        for _ in pay_sup:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "supply_app.html", context=error_message_empty)

        count_name = 0
        for _ in date:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "supply_app.html", context=error_message_empty)

        try:
            supply = Suppliers.objects.get(name=f"{name}")
            print(supply)
        except:
            return render(request, "supply_app.html", context=error_message_empty)

        new_supply = supply.supply_set.create(amount=f"{pay_sup}", date=f"{date}")
        new_supply.save()
        return render(request, "supply_app.html", context=message)


def suppliers_app(request):
    if request.method == "GET":
        dat = Suppliers.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 3:
                new_dat.append(i)
            elif count == 4:
                # new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")

        suppliers_list = {"suppliers_list": str(new_dat2)}
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
    elif request.method == "POST":
        message = {"message": "Поставщик удален."}
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}
        data = request.POST.get
        print(data)
        name = data("name")
        print(name)
        count_name = 0
        for _ in name:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "suppliers_app.html", context=error_message_empty)
        supplier_del = Suppliers.objects.get(name=f"{name}")
        print(supplier_del)
        return render(request, "suppliers_app.html", context=message)


def production_app(request):
    return render(request, "production_app.html")


def bid_app(request):
    if request.method == "GET":
        return render(request, "bid_app.html")
    elif request.method == "POST":
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}
        message = {"message": "Заявка отправлена."}
        data = request.POST.get
        print(data)
        text = data("text")
        print(text)
        date = datetime.date
        print(date)
        count_name = 0
        for _ in text:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "bid_app.html", context=error_message_empty)

        return render(request, "bid_app.html", context=message)
