"""
    imports  -------------site_pages apps.py----------------------
"""
# third party imports
from django.apps import AppConfig


class SitePagesConfig(AppConfig):
    """
    Django config class for site_pages app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_pages'
