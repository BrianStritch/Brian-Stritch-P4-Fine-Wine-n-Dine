"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
# internal imports
from bookings.forms import BookingForm


class TestBookingsForm(TestCase):
    """
        Class for testing the Create Review Form
    """

    def test_create_booking_form(self):
        """
        Test for testing form validation of the Create Review form
        """

        test_booking_form_data = {
            'booking_date': 'test_booking_date',
            'Meal_time': 'test_meal_time',
            'number_of_guests': 'test_number_of_guests',
            'dietary_notes': 'test_dietary_notes',
            'additional_comments': 'test_additional_comments',
        }

        form = BookingForm(test_booking_form_data)
        self.assertTrue(form.is_valid)
