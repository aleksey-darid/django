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
        url = reverse("user-list")
        response = self.client.get(url)
        serializer_data = UserSerializer([user_1, user_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

