from django import forms
from .models import Booking
# from .widgets import DateTimePickerInput


class BookingForm(forms.ModelForm):
    # Post = Booking

    class Meta:
        model = Booking
        # my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
        # fields = ('Meal_time', 'number_of_guests', 'dietary_notes', 'additional_comments',)  # noqa
        fields = ('booking_date','Meal_time', 'number_of_guests', 'dietary_notes', 'additional_comments',)  # noqa
        
        widgets = {
            'dietary_notes': forms.Textarea(attrs={'cols': 20, 'rows': 2}),
            'additional_comments': forms.Textarea(attrs={'cols': 20, 'rows': 2}),
            # 'Meal_time': forms.TextInput(attrs={
            #     'type': 'time',
            #     'min': '09:00',
            #     'max': '18:00',
            #       'step': '3600',
            #     }),
            'booking_date': forms.TextInput(attrs={'type': 'date'}),
            'number_of_guests': forms.TextInput(attrs={
                'type': 'number',
                'min': '0',
                'max': '10',
                })

    }


    # type="time" id="appt" name="appt"
    #     max="18:00" required
