from django.test import TestCase
from bookings.forms import BookingForm
import unittest


class Test_bookings_form(TestCase):

    def test_Create_booking_form(self):
        '''
        Test for testing form validation of the Create Review form
        '''

        data = {
            'booking_date': 'test_booking_date',
            'Meal_time': 'test_meal_time',
            'number_of_guests': 'test_number_of_guests',
            'dietary_notes': 'test_dietary_notes',
            'additional_comments': 'test_additional_comments',
            
        }

        form = BookingForm(data)
        self.assertTrue(form.is_valid)



