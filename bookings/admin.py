"""
    imports  ------Bookings admin.py----------------------
"""
# third party imports
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# internal imports
from .models import Booking


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel
    """

    list_display = (
        'primary_guest',
        'availability',
        'booking_status',
        'booking_created_on',
        'booking_date',
        'Meal_time',
        )

    list_filter = (
        'booking_status',
        'booking_date'
        )

    search_fields = [
        'primary_guest',
        'Meal_time',
        'booking_date',
        ]

    summernote_fields = (
        'dietary_notes',
        'additional_comments'
        )
