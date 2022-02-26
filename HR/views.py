from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from .models import Schedule
from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer


class ScheduleView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


def schedule_app(request):
    url_api = "http://127.0.0.1:8000/api/schedule/"
    try:
        if request.POST:
            w_h1 = float(request.POST.get("work_hours1").replace(":", "."))
            w_h2 = float(request.POST.get("work_hours2").replace(":", "."))
            print(w_h1, w_h2)
            data = {"message": "Время работы успешно записано"}
            return render(request, "schedule_app.html", context=data)
        else:
            return render(request, "schedule_app.html")

    except:
        return render(request, "schedule_app.html")


