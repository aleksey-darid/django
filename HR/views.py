from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Schedule
from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer
from .forms import ScheduleForm


class ScheduleView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


def schedule_app(request):
    if request.method == "GET":
        ses_user2 = request.user.username
        form = ScheduleForm()
        worker = {"worker": ses_user2, "form": form}
        return render(request, "schedule_app.html", context=worker)
    elif request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            dt = (form.cleaned_data.get("date_from").seconds - form.cleaned_data.get("date_to")).seconds
            print(dt)
            sch1 = Schedule(**form.cleaned_data, worker=request.user, delta=dt)
            print(sch1)
            sch1.save()
        return redirect("schedule")

    """date = request.POST.get("date").replace("-", ".")
    print(date)
    w_h1 = float(request.POST.get("work_hours1").replace(":", "."))
    w_h2 = float(request.POST.get("work_hours2").replace(":", "."))
    print(w_h1, w_h2)
    data = {"message": "Время работы успешно записано"}
    return render(request, "schedule_app.html", context=data)
    # error_message = {"error_message": "POST не обработался"}
    # return render(request, "schedule_app.html", context=error_message)"""
