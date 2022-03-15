from django import forms
from .models import Booking
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class BookingForm(forms.ModelForm):
    #Post = Booking

    class Meta:
        model = Booking
        fields = ('booking','number_of_guests', 'dietary_notes',)
        
