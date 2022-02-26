from django.shortcuts import render


def base_app(request):
    return render(request, "base_app.html")


def home_app(request):
    return render(request, "home_app.html")
