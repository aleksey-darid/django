from inspect import Traceback
from django.contrib.auth.models import Group, Permission
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def registration_app(request):
    """Используется система аутентификации и авторизации django"""
    if request.method == "GET":
        return render(request, "registration_app.html")
    elif request.method == "POST":
        message = {"message": "Вы добавлены в систему!"}
        error_message = {"error_message": "Вы уже зарегестрированы в системе, перейдите на страницу входа"}
        error_message_pas = {"error_message_pas": "Такое имя пользователя уже есть"
                                                  "Ваш пароль не может быть слишком похож на другую вашу личную информацию."
                                                  "Ваш пароль должен содержать не менее 8 символов."
                                                  "Ваш пароль не может быть широко используемым паролем."
                                                  "Ваш пароль не может быть полностью числовым."}
        # error_message_phone = {"error_message_phone": "Такая почта уже есть!"}
        error_message_empty = {"error_message_empty": "Поля не могут быть пустыми."}

        username = request.POST['username']  # Получаем знычение username
        password = request.POST['password']  # Получаем знычение password
        email = request.POST['email']  # Получаем знычение email
        print(username, password, email)

        count_name = 0  # Проверяем поля на заполненность
        for _ in username:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        count_name = 0  # Проверяем поля на заполненность
        for _ in password:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        count_name = 0  # Проверяем поля на заполненность
        for _ in email:
            count_name = count_name + 1
        if count_name == 0:
            return render(request, "registration_app.html", context=error_message_empty)

        user = authenticate(request, username=username, password=password,
                            email=email)  # Проверяем есть ли такой пользователь
        print(user)
        if user is not None:
            return render(request, "registration_app.html",
                          context=error_message)  # Если такой пользователь есть - предлагаем осуществить вход
        else:
            try:
                new_user = User.objects.create(username=f"{username}", password=f"{password}",
                                               email=f"{email}")  # Создаем пользователя
                print(new_user)
                new_user.save()
                new_user.groups.add(Group.objects.get(name='Users'))  # Определяем его в нужную нам группу
                return render(request, "registration_app.html", context=message)
            except:
                return render(request, "registration_app.html", context=error_message_pas)


def login_app(request):
    """Используется система аутентификации и авторизации django"""
    if request.method == "GET":
        return render(request, "login_page.html")
    elif request.method == "POST":
        message = {"message": "Вы вошли в систему!"}
        error_message = {"error_message": "Не верный логин или пароль, попробуйте снова или зарегестрируйтесь"}
        username = request.POST['username']  # Получаем знычение username
        password = request.POST['password']  # Получаем знычение password

        user = authenticate(request, username=username, password=password)  # Проверяем есть ли такой пользователь
        if user is not None:
            login(request, user)  # Если такой пользователь есть - осуществляем привязку к сессии
            return render(request, "login_page.html", context=message)
        else:
            return render(request, "login_page.html", context=error_message)


def logout_app(request):
    if request.method == "GET":
        return render(request, "logout_page.html")
    elif request.method == "POST":
        logout_message = {"logout_message": "Вы вышли из системы"}
        logout(request)
        return render(request, "logout_page.html", context=logout_message)


def user_app(request):
    if request.method == "GET":
        dat = User.objects.in_bulk()
        print(dat, dat.values())
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []

        count = 0
        for i in dat_list:
            count += 1
            if count == 2:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">", "").replace(")", "")
        users_list = {"users_list": new_dat2}
        return render(request, "users_app.html", context=users_list)
    return render(request, "users_app.html")


def workers_app(request):
    if request.method == "GET":
        dat = User.objects.filter(groups__name="Workers")
        dat_list1 = str(dat.values()).replace(":", ",").split(",")
        print(dat_list1)
        dat_list = list(dat_list1)
        new_dat = []
        count = 0
        for i in dat_list:
            count += 1
            if count == 10:
                new_dat.append(i)
            elif count == 38:
                new_dat.append(i)
                count = 0
        new_dat2 = str(new_dat).replace("'", "").replace("[", "").replace("]", "").replace(">",
                                                                                           "").replace(")",
                                                                                                       "").replace('"',
                                                                                                                   "")
        workers_list = {"workers_list": new_dat2}
        return render(request, "workers_app.html", context=workers_list)
    return render(request, "workers_app.html")


def administration_app(request):
    return render(request, "administration_app.html")
