from django.test import TestCase

from Users.models import Users, Workers, Administration
from Users.serializers import UsersSerializer, WorkersSerializer


class UsersSerializerTestCase(TestCase):
    def test_ok(self):
        user_1 = Users.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                      email="sd@kail.ru")
        user_2 = Users.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                      email="pollisuchka@gmail.com")
        data = UsersSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "name": "Павел",
                "password": "123tS76",
                "phone_number": "+375291565387",
                "email": "sd@kail.ru"
            },
            {
                # "id": user_2.id,
                "name": "Polli",
                "password": "sisatS76",
                "phone_number": "+375-29-1565387",
                "email": "pollisuchka@gmail.com"
            }
        ]
        self.assertEqual(expected_data, data)


class WorkersSerializerTestCase(TestCase):
    def test_ok(self):
        worker_1 = Workers.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                          email="sd@kail.ru", rate_per_hour=4)
        worker_2 = Workers.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                          email="pollisuchka@gmail.com", rate_per_hour=5)
        data = WorkersSerializer([worker_1, worker_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "name": "Павел",
                "password": "123tS76",
                "phone_number": "+375291565387",
                "email": "sd@kail.ru",
                "rate_per_hour": 4
            },
            {
                # "id": user_2.id,
                "name": "Polli",
                "password": "sisatS76",
                "phone_number": "+375-29-1565387",
                "email": "pollisuchka@gmail.com",
                "rate_per_hour": 5
            }
        ]
        self.assertEqual(expected_data, data)


class AdministrationSerializerTestCase(TestCase):
    def test_ok(self):
        admin_1 = Administration.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                                email="sd@kail.ru")
        admin_2 = Administration.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                                email="pollisuchka@gmail.com")
        data = UsersSerializer([admin_1, admin_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "name": "Павел",
                "password": "123tS76",
                "phone_number": "+375291565387",
                "email": "sd@kail.ru"
            },
            {
                # "id": user_2.id,
                "name": "Polli",
                "password": "sisatS76",
                "phone_number": "+375-29-1565387",
                "email": "pollisuchka@gmail.com"
            }
        ]
        self.assertEqual(expected_data, data)
