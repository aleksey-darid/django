from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Users, Workers, Administration
from .serializers import UsersSerializer, WorkersSerializer, AdministrationSerializer


class UsersView(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class WorkersView(ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer


class AdministrationView(ModelViewSet):
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer


def users_app(request):
    return render(request, "users_app.html")


def workers_app(request):
    return render(request, "workers_app.html")


def administration_app(request):
    return render(request, "administration_app.html")