from rest_framework.serializers import ModelSerializer

from .models import Users, Workers, Administration


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ["name", "password", "phone_number", "email"]


class WorkersSerializer(ModelSerializer):
    class Meta:
        model = Workers
        fields = ["name", "password", "phone_number", "email", "rate_per_hour"]


class AdministrationSerializer(ModelSerializer):
    class Meta:
        model = Administration
        fields = ["name", "password", "phone_number", "email"]
