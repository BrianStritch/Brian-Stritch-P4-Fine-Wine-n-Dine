from django.test import TestCase
from bookings.models import Booking
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class TestBookingModel(TestCase):

    def test_model_slugify(self):
        query = User.objects.all()
        user = query.filter(is_superuser=True)
        test_slug = Booking.objects.create(primary_guest=user, booking_date='2022-03-28', Meal_time=3)
        self.assertEqual(
            slugify(
                f"{self.primary_guest}_{self.booking_date}_{self.Meal_time}"
                ),
                'Django-Testing_2022-03-28_3')