from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
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

            # 'Meal_time': forms.TextInput(attrs={
            #     'type': 'time',
            #     'min': '09:00',
            #     'max': '18:00',
            #       'step': '3600',
            #     }),

            'booking_date': forms.TextInput(
                attrs={
                    'type': 'date',
                    'data-date-format': 'dd-mm-yyyy',
                    }),

            'number_of_guests': forms.TextInput(
                attrs={
                    'type': 'number',
                    'min': '0',
                    'max': '10',
                    })
        }





