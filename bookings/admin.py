from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

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
