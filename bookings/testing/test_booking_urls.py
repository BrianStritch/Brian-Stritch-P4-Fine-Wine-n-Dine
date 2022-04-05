"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
from django.contrib.auth.models import User
# internal imports
from bookings.models import Booking


class TestBookingsUrls(TestCase):
    """
    Class for testing booking urls
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

    def test_bookings_page_url(self):

        """
        This test checks that the bookings page
        is displayed using the correct URL
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/bookings/')
        self.assertTemplateUsed('bookings/bookings.html')
        self.assertEqual(response.status_code, 200)

    def test_edit_bookings_page_url(self):

        """
        This test checks that the edit bookings page
        is displayed using the correct URL
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/edit_booking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_booking.html')

    def test_delete_booking_page_url(self):

        """
        This test checks that the delete bookings page
        is displayed using the correct URL
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/delete_booking/1/')
        self.assertTemplateUsed('bookings/delete_booking.html')
        self.assertEqual(response.status_code, 200)

    def test_create_a_booking_page_url(self):
        """
        This test checks that the create_a_booking page
        is displayed using the correct URL
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/create_a_booking/')
        self.assertTemplateUsed('bookings/create_a_booking.html')
        self.assertEqual(response.status_code, 200)

    def test_get_admin_bookings_page(self):
        """
        This test checks that the admin_bookings page
        is displayed using the correct URL
        """
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/bookings/admin_bookings_view/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/admin_bookings_view.html')
