from datetime import datetime

import datetime
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
            df = datetime.datetime.strptime(str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_from")),
                                            "%Y-%m-%d%H:%M:%S")
            dt = datetime.datetime.strptime(str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_to")),
                                            "%Y-%m-%d%H:%M:%S")
            delta = (dt - df).seconds / 60
            print(df, dt, delta)
            sch1 = Schedule(**form.cleaned_data, worker=request.user, delta=delta)
            print(sch1)
            sch1.save()
        return redirect("schedule")

