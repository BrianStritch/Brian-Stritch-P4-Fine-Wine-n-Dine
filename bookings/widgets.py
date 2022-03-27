from django import forms
from fine_wine_n_dine import settings

class DateInput(forms.DateInput):
    input_type = 'date'
    # input_formats=settings.DATE_INPUT_FORMATS
    input_formats=['%d-%m-%Y']
