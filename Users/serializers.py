from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]


"""class WorkersSerializer(ModelSerializer):
    class Meta:
        model = Workers
        fields = ["name", "password", "phone_number", "email", "rate_per_hour"]


class AdministrationSerializer(ModelSerializer):
    class Meta:
        model = Administration
        fields = ["name", "password", "phone_number", "email"]"""
