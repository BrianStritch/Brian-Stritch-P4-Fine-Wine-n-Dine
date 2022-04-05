"""
    imports  -------------------------------------------------------
"""
# third party imports
from django import forms
from .widgets import DateInput
# internal imports
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Class based form to create new bookings using the
    bookings model
    """

    class Meta:
        """
        Class to set the fields in the booking model form,
        and the additional widgets to set the attributes of the
        fields
        """
        model = Booking
        fields = (
            'booking_date',
            'Meal_time',
            'number_of_guests',
            'dietary_notes',
            'additional_comments',
            )

        widgets = {
            'dietary_notes': forms.Textarea(
                attrs={
                    'cols': 20,
                    'rows': 2,
                    }),

            'additional_comments': forms.Textarea(
                attrs={
                    'cols': 20,
                    'rows': 2,
                    }),
            'booking_date': DateInput(),

            'number_of_guests': forms.TextInput(
                attrs={
                    'type': 'number',
                    'min': '0',
                    'max': '10',
                    })
        }
