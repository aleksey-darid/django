from rest_framework.serializers import ModelSerializer

from .models import Schedule


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["worker", "date", "time_from", "time_to", "delta"]





