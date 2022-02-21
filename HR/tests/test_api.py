from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from HR.models import Schedule
from HR.serializers import ScheduleSerializer
from Users.models import Workers


class HRApiTestCase(APITestCase):
    def test_get(self):
        worker_1 = Workers.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                          email="sd@kail.ru", rate_per_hour=4)
        worker_2 = Workers.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                          email="pollisuchka@gmail.com", rate_per_hour=5)
        record_1 = Schedule.objects.create(data="2022-02-10", worker=worker_1, hours=14.5)
        record_2 = Schedule.objects.create(data="2022-02-11", worker=worker_2, hours=7.5)
        url = reverse("schedule-list")
        response = self.client.get(url)
        serializer_data = ScheduleSerializer([record_1, record_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)



