"""
    imports  ------Reviews apps.py----------------------
"""
# third party imports
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """
    Django config class for Reviews app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'
