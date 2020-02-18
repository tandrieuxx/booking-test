from datetime import datetime

from django.test import TestCase
from pytz import timezone

from booking.models import Booking


class BookingModelTest(TestCase):
    fixtures = ["initial.json"]

    def setUp(self):
        Booking.objects.create(
            title="test1",
            resource_id=1,
            start_date=datetime(2020, 3, 1, 8, tzinfo=timezone("UTC")),
            end_date=datetime(2020, 3, 1, 10, tzinfo=timezone("UTC")),
            user_id=1,
        )
        Booking.objects.create(
            title="test2",
            resource_id=1,
            start_date=datetime(2020, 3, 1, 11, tzinfo=timezone("UTC")),
            end_date=datetime(2020, 3, 1, 12, tzinfo=timezone("UTC")),
            user_id=1,
        )
        Booking.objects.create(
            title="test3",
            resource_id=2,
            start_date=datetime(2020, 3, 1, 15, tzinfo=timezone("UTC")),
            end_date=datetime(2020, 3, 1, 17, tzinfo=timezone("UTC")),
            user_id=1,
        )

    def test_check_overlap(self):
        result = Booking.check_overlap(
            1,
            datetime(2020, 3, 1, 14, tzinfo=timezone("UTC")),
            datetime(2020, 3, 1, 18, tzinfo=timezone("UTC")),
        )
        self.assertFalse(result)

        result = Booking.check_overlap(
            1,
            datetime(2020, 3, 1, 7, tzinfo=timezone("UTC")),
            datetime(2020, 3, 1, 11, 30, tzinfo=timezone("UTC")),
        )
        self.assertTrue(result)

        result = Booking.check_overlap(
            1,
            datetime(2020, 3, 1, 10, tzinfo=timezone("UTC")),
            datetime(2020, 3, 1, 14, tzinfo=timezone("UTC")),
        )
        self.assertTrue(result)
