"""
    imports  ------Bookings apps.py----------------------
"""
# third party imports
from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Django config class for bookings app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
