from django.test import TestCase
from bookings.models import Booking
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class TestBookingModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            id=1,
            email='test@test.com',
            username='test_username',
            password='testpassword',
            first_name='test_first',
            last_name='test_last'
        )

    def test_model_slugify(self):        
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        test_slug = Booking.objects.create(primary_guest=user, booking_date='2022-03-28', Meal_time=3)
        self.assertEqual(
            slugify(
                f"{self.primary_guest}_{self.booking_date}_{self.Meal_time}"
                ),
                'test_username_2022-03-28_3')