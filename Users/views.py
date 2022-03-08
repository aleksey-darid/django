from inspect import Traceback

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Users, Workers, Administration
from .serializers import UsersSerializer, WorkersSerializer, AdministrationSerializer
from .forms import LoginForm


class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class WorkersView(ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer


class AdministrationView(ModelViewSet):
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer


def registration_app(request):
    if request.method == "GET":
        return render(request, "registration_app.html")
    elif request.method == "POST":
        message = {"message": "Вы добавлены в систему!"}
        error_message = {"error_message": "Вы уже зарегестрированы в системе!"}
        error_message_pas = {"error_message_pas": "Введите другой пароль, этот занят)"}
        error_message_phone = {"error_message_phone": "Такой номер уже есть!"}
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}
        data = request.POST.get
        print(data)
        name = data("name")
        print(name)
        password = data("password")
        print(password)
        phone_num = data("phone")
        print(phone_num)

        count_name = 0
        for _ in name:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        count_pas = 0
        for _ in password:
            count_pas = count_pas + 1
        if count_pas == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        count_ph_n = 0
        for _ in phone_num:
            count_ph_n = count_ph_n + 1
        if count_ph_n == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        try:
            name_get = Users.objects.get(name=f"{name}").name
            pas_get = Users.objects.get(password=f"{password}").password
            ph_n_get = Users.objects.get(phone_number=f"{phone_num}").phone_number
            return render(request, "registration_app.html", context=error_message)
        except:
            try:
                pas_get = Users.objects.get(password=f"{password}").password
                print(pas_get)
                return render(request, "registration_app.html", context=error_message_pas)
            except:
                try:
                    ph_n_get = Users.objects.get(phone_number=f"{phone_num}").phone_number
                    print(ph_n_get)
                    return render(request, "registration_app.html", context=error_message_phone)
                except:
                    new_user = Users.objects.create(name=f"{name}", password=f"{password}", phone_number=f"{phone_num}")
                    new_user.save()
                    print(name, password, phone_num)
                    return render(request, "registration_app.html", context=message)


def login_app(request):
    message = {"message": "Вы работник!"}
    error_message = {"error_message": "Вас нет в списке работников!"}

    # Первый способ получить значения из запроса
    login = request.POST.get("name")
    password = request.POST.get("password")
    print(login, password)

    # Взятие из модели -обьекта по значениям из запроса
    try:
        m_login = Workers.objects.get(name=f"{login}").name
        m_password = Workers.objects.get(password=f"{password}").password
        print(m_login, m_password)
    except:
        return render(request, "login_page.html", context=error_message)

    # Второй способ получить знаяения из запроса
    log = LoginForm(request.POST)["name"].value()
    pas = LoginForm(request.POST)["password"].value()
    print(log, pas)

    # Взятие из модели -обьекта по значениям из запроса
    try:
        m_log = Workers.objects.get(name=f"{log}").name
        m_pas = Workers.objects.get(password=f"{pas}").password
        print(m_log, m_pas)
    except:
        return render(request, "login_page.html", context=error_message)

    try:
        if m_log:
            if m_pas:
                return render(request, "login_page.html", context=message)
        else:
            return render(request, "login_page.html", context=error_message)
    except:
        return render(request, "login_page.html", context=error_message)


def users_app(request):
    if request.method == "GET":
        dat = Users.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []

        count = 0
        for i in dat_list:
            count += 1
            if count == 3:
                new_dat.append(i)
            elif count == 5:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        users_list = {"users_list": new_dat2}
        return render(request, "users_app.html", context=users_list)
    return render(request, "users_app.html")


def workers_app(request):
    if request.method == "GET":
        dat = Workers.objects.in_bulk()
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []

        count = 0
        for i in dat_list:
            count += 1
            if count == 3:
                new_dat.append(i)
            elif count == 5:
                new_dat.append(i)
            elif count == 6:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        workers_list = {"workers_list": new_dat2}
        return render(request, "workers_app.html", context=workers_list)
    return render(request, "workers_app.html")


def administration_app(request):
    return render(request, "administration_app.html")
