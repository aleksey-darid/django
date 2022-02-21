from django.shortcuts import render


def home_app(request):
    return render(request, "home_app.html")
