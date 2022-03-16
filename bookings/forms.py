from django import forms
from .models import Booking
# from .widgets import DateTimePickerInput


class BookingForm(forms.ModelForm):
    # Post = Booking

    class Meta:
        model = Booking
        # my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
        fields = ('Meal_time', 'number_of_guests', 'dietary_notes', 'additional_comments',)  # noqa
        # fields = ('my_date_time_field', 'dietary_notes',)

        # widgets = {
            
        #     'my_date_time_field' : DateTimePickerInput(),
        # }
