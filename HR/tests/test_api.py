from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from HR.models import Schedule
from HR.serializers import ScheduleSerializer
from Users.models import Workers


class HRApiTestCase(APITestCase):
    def test_get(self):
        worker_1 = User.objects.create(username="Павел", password="123tS76",
                                          email="sd@kail.ru")
        worker_2 = User.objects.create(username="Polli", password="sisatS76",
                                          email="pollisuchka@gmail.com")
        record_1 = Schedule.objects.create(date="2022-02-10", worker=worker_1, time_from="14:45:00", time_to="14:46:00",
                                           delta=1)
        record_2 = Schedule.objects.create(date="2022-02-11", worker=worker_2, time_from="14:45:00", time_to="14:47:00",
                                           delta=2)
        url = reverse("schedule-list")
        response = self.client.get(url)
        serializer_data = ScheduleSerializer([record_1, record_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)



