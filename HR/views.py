from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .models import Schedule
from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer


class ScheduleView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


def schedule_app(request):
    return render(request, "schedule_app.html")
