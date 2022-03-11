from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Users.serializers import UserSerializer
from django.contrib.auth.models import User


class UsersApiTestCase(APITestCase):
    def test_users_get(self):
        user_1 = User.objects.create(username="Павел", password="123tS76",
                                     email="sd@kail.ru")
        user_2 = User.objects.create(username="Polli", password="sisatS76",
                                     email="pollisuchka@gmail.com")
        url = reverse("users-list")
        response = self.client.get(url)
        serializer_data = UserSerializer([user_1, user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class WorkersApiTestCase(APITestCase):
    def test_workers_get(self):
        worker_1 = Workers.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                          email="sd@kail.ru", rate_per_hour=4)
        worker_2 = Workers.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                          email="pollisuchka@gmail.com", rate_per_hour=5)
        url = reverse("workers-list")
        response = self.client.get(url)
        serializer_data = WorkersSerializer([worker_1, worker_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class AdministrationApiTestCase(APITestCase):
    def test_administration_get(self):
        admin_1 = Administration.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                                email="sd@kail.ru")
        admin_2 = Administration.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                                email="pollisuchka@gmail.com")
        url = reverse("administration-list")
        response = self.client.get(url)
        serializer_data = AdministrationSerializer([admin_1, admin_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
