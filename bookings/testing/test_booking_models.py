"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
# internal imports
from bookings.models import Booking


class TestBookingModel(TestCase):
    """
        Class for testing booking model
    """

    @classmethod
    def setUpTestData(cls):

        """
            classmethod creating a user and booking instances for use in
            the testing below
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
            booking_date='2022-03-30',
            Meal_time=2,
        )
        booking.save()

    def test_booking_model_slugify(self):
        """
            tests to check that the booking model slug is
            created in the correct format
        """
        booking = Booking.objects.get(booking_date='2022-03-30')
        self.client.login(username='test_username', password='testpassword')
        self.assertEqual(
            slugify(
                f"\
                    {booking.primary_guest}_{booking.booking_date}_{booking.Meal_time}\
                        "), 'test_username_2022-03-30_2')

    # 2
    def test_create_booking(self):
        """
            tests to verify that the create booking model saves
            to the database
        """
        user = User.objects.get(id=1)
        booking = Booking(
            primary_guest=user,
            booking_date='2023-04-30',
            Meal_time=2,
        )
        booking.save()
        self.assertTrue(booking.save)

    # 3
    def test_edit_booking(self):
        """
            tests to verify that the booking can be edited and saved
            to the database
        """
        booking = Booking.objects.get(booking_date='2022-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date='2022-03-30')
        self.assertEqual(booking.Meal_time, 3)

    # 4
    def test_delete_booking(self):
        """
            tests for delete booking to verify that the booking can be deleted
            from the database
        """
        booking = Booking.objects.get(booking_date='2022-03-30')
        self.assertTrue(booking.delete)

    # 5
    def test_edit_booking_front_end(self):
        """
            tests for front end edit booking page
        """
        booking = Booking.objects.get(booking_date='2022-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date='2022-03-30')
        self.assertEqual(booking.Meal_time, 3)
        response = self.client.post(
            reverse('edit_booking', kwargs={'pk': booking.id}),
            {'booking.Meal_time': '3'})
        self.assertEqual(response.status_code, 200)

    # 6
    def test_delete_booking_page(self):
        """
            tests for front end delete booking page to test
            that the boooking is deleted and the page does not exist
            after deleting.
        """
        booking = Booking.objects.get(booking_date='2022-03-30')
        response = self.client.post(
            reverse(
                'delete_booking',
                kwargs={'pk': booking.id}),
            )
        self.assertTrue(booking.delete)
        self.assertEqual(response.status_code, 302)

    # 7
    def test_create_a_booking_page(self):
        """
            tests for create a booking view to test that:
            user is logged in and authenticated,
            creates a new booking ,
            checks the page status when rendered,
            tests which template used to render page,
            tests if the rendered page has the relevant data,
            ie. title, Meal_time, Booking_date, slug, and reverse url
        """
        user = User.objects.get(id=1)
        booking = Booking(
            primary_guest=user,
            booking_date='2024-03-30',
            Meal_time=5,
            )
        booking.save()
        self.assertTrue(booking.save)
        url = reverse('create_a_booking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_a_booking.html')
        self.assertContains(response, 'title')
        self.assertContains(response, 'booking_date')
        self.assertContains(response, 'Meal_time')
        self.assertTrue(booking.primary_guest, 'request.user')
        self.assertTrue(reverse('bookings'))
        self.assertEqual(
            booking.slug,
            f"{booking.primary_guest}_{booking.booking_date}_{booking.Meal_time}") # noqa

    # 8
    def test_view_all_my_bookings_page(self):
        """
            tests for front end bookings page to test that:
            user is logged in and authenticated,
            gets all bookings realtive to the logged in user,
            checks the page status when rendered,
            tests which template used to render page.

        """
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        self.assertTrue(user.is_authenticated)
        url = reverse('bookings')
        page = self.client.get(url)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'bookings/bookings.html')
