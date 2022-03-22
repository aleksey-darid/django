from datetime import datetime

import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Schedule, Wages
from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer
from .forms import ScheduleForm, WagesForm
from Users.models import Workers


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
            df = datetime.datetime.strptime(
                str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_from")),
                "%Y-%m-%d%H:%M:%S")
            dt = datetime.datetime.strptime(str(form.cleaned_data.get("date")) + str(form.cleaned_data.get("time_to")),
                                            "%Y-%m-%d%H:%M:%S")
            delta = (dt - df).seconds / 60
            print(df, dt, delta)
            sch1 = Schedule(**form.cleaned_data, worker=request.user, delta=delta)
            print(sch1)
            sch1.save()
        return redirect("schedule")


def wages_app(request):
    if request.method == "GET":
        form = WagesForm()
        form_html = {"form": form}
        return render(request, "wages_app.html", context=form_html)
    elif request.method == "POST":
        form = WagesForm(request.POST)
        if form.is_valid():
            worker = form.cleaned_data.get("worker")
            date_from = form.cleaned_data.get("date_from")
            date_to = form.cleaned_data.get("date_to")
            days_list = list()
            work_days = Schedule.objects.filter(worker=worker)
            for i in work_days:
                if i.date >= date_from and i.date <= date_to:
                    days_list.append(i)
            delta_list = list()
            for i in days_list:
                delta_list.append(i.delta)
            s = 0
            for i in delta_list:
                s += i
            hours = s / 60
            r_p_h = int(request.user.workers.rate_per_hour)
            print(r_p_h)
            pay = hours * r_p_h
            pay1 = {"pay": pay, "pay_text": "Ваша ЗП за выбраный период составит -", "r": "р."}
            sch1 = Wages(**form.cleaned_data, hours=hours, total_wages=pay)
            print(sch1)
            sch1.save()
            return render(request, "wages_app.html", context=pay1)
    return redirect("wages")
