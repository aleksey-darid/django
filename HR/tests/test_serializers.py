from django.contrib.auth.models import User
from django.test import TestCase

from HR.models import Schedule
from HR.serializers import ScheduleSerializer


class ScheduleSerializerTestCase(TestCase):
    def test_ok(self):
        worker_1 = User.objects.create(username="Павел", password="123tS76",
                                       email="sd@kail.ru")
        worker_2 = User.objects.create(username="Polli", password="sisatS76",
                                       email="pollisuchka@gmail.com")
        record_1 = Schedule.objects.create(date="2022-02-10", worker=worker_1, time_from="14:45:00", time_to="14:46:00",
                                           delta=1)
        record_2 = Schedule.objects.create(date="2022-02-11", worker=worker_2, time_from="14:45:00", time_to="14:47:00",
                                           delta=2)
        data = ScheduleSerializer([record_1, record_2], many=True).data
        expected_data = [
            {
                "date": "2022-02-10",
                "worker": 1,
                "time_from": "14:45:00",
                "time_to": "14:46:00",
                "delta": 1

            },
            {
                "date": "2022-02-11",
                "worker": 2,
                "time_from": "14:45:00",
                "time_to": "14:47:00",
                "delta": 2
            }
        ]
        self.assertEqual(expected_data, data)
