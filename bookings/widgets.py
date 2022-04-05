"""
    imports  -------------------------------------------------------
"""
# third party imports
from django import forms


class DateInput(forms.DateInput):
    """
    Class used to set values in widget for
    bookings form
    """
    input_type = 'date'
    input_formats = ['%d-%m-%Y']
