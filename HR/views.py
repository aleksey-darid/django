from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Schedule
from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer


class ScheduleView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


def schedule_app(request):
    if request.method == "GET":
        ses_user2 = request.session.get("_auth_user_id")
        worker = {"worker": f"{str(ses_user2)}"}
        return render(request, "schedule_app.html", context=worker)
    elif request.method == "POST":
        ses_user = request.session.keys()
        print(ses_user)
        ses_user1 = request.session.get("_auth_user_id")
        print(ses_user1)
        ses_user2 = request.session.get("_auth_user_backend")
        print(ses_user2)
        worker = {"worker": f"{str(ses_user2)}"}
        ses_user3 = request.session.get("_auth_user_hash")
        print(ses_user3)
        return render(request, "schedule_app.html", context=worker)



        """date = request.POST.get("date").replace("-", ".")
        print(date)
        w_h1 = float(request.POST.get("work_hours1").replace(":", "."))
        w_h2 = float(request.POST.get("work_hours2").replace(":", "."))
        print(w_h1, w_h2)
        data = {"message": "Время работы успешно записано"}
        return render(request, "schedule_app.html", context=data)
        # error_message = {"error_message": "POST не обработался"}
        # return render(request, "schedule_app.html", context=error_message)"""



