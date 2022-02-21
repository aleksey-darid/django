from django.test import TestCase

from HR.models import Schedule
from HR.serializers import ScheduleSerializer
from Users.models import Workers


class ScheduleSerializerTestCase(TestCase):
    def test_ok(self):
        worker_1 = Workers.objects.create(name="Павел", password="123tS76", phone_number="+375291565387",
                                          email="sd@kail.ru", rate_per_hour=4)
        worker_2 = Workers.objects.create(name="Polli", password="sisatS76", phone_number="+375-29-1565387",
                                          email="pollisuchka@gmail.com", rate_per_hour=5)
        record_1 = Schedule.objects.create(data="2022-02-10", worker=worker_1, hours=14.5)
        record_2 = Schedule.objects.create(data="2022-02-11", worker=worker_2, hours=7.5)
        data = ScheduleSerializer([record_1, record_2], many=True).data
        expected_data = [
            {
                # "id": user_1.id,
                "data": "2022-02-10",
                "worker": 1,
                # "worker.name": "Павел",
                # "worker.password": "123tS76",
                # "worker.phone_number": "+375291565387",
                # "worker.email": "sd@kail.ru",
                # "worker.rate_per_hour": 4,
                "hours": "14.5"

            },
            {
                # "id": user_2.id,
                "data": "2022-02-11",
                "worker": 2,
                # "worker.name": "Polli",
                # "worker.password": "sisatS76",
                # "worker.phone_number": "+375-29-1565387",
                # "worker.email": "pollisuchka@gmail.com",
                # "worker.rate_per_hour": 5,
                "hours": "7.5"
            }
        ]
        self.assertEqual(expected_data, data)
