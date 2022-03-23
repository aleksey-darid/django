from django.contrib.auth.models import User
from django.test import TestCase

from Users.serializers import UserSerializer


class UsersSerializerTestCase(TestCase):
    def test_ok(self):
        user_1 = User.objects.create(username="Павел", password="123tS76",
                                      email="sd@kail.ru")
        user_2 = User.objects.create(username="Polli", password="sisatS76",
                                      email="pollisuchka@gmail.com")
        data = UserSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "username": "Павел",
                "password": "123tS76",
                "email": "sd@kail.ru"
            },
            {
                # "id": user_2.id,
                "username": "Polli",
                "password": "sisatS76",
                "email": "pollisuchka@gmail.com"
            }
        ]
        self.assertEqual(expected_data, data)
