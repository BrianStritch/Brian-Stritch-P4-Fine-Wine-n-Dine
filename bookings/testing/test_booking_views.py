"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
from django.contrib.auth.models import User
# internal imports
from bookings.models import Booking


class TestBookingView(TestCase):
    """
    A class for testing create_booking page views
    """
    @classmethod
    def setUpTestData(cls):
        """
        classmethod creating a user and booking instances for testing
        """
        user = User.objects.create_user(
                id=1,
                email='test@test.com',
                username='test_username',
                password='testpassword',
                first_name='test_first',
                last_name='test_last'
            )
        user.save()
        booking = Booking(
            primary_guest=user,
            booking_date='2023-03-30',
            Meal_time=2,
        )
        booking.save()

    def test_get_create_booking_page(self):
        """
        This test checks that the edit_booking page
        is displayed correctly
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/create_a_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_a_booking.html')

    def test_get_bookings_page(self):
        """
        This test checks that the bookings page
        is displayed correctly
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/bookings.html')

    def test_get_edit_booking_page(self):
        """
        This test checks that the edit_booking page
        is displayed correctly
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/edit_booking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_booking.html')

    def test_get_admin_bookings_page(self):
        """
        This test checks that the admin_bookings page
        is displayed correctly
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/admin_bookings_view/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/admin_bookings_view.html')
