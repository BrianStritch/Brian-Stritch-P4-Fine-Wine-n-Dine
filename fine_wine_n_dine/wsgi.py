"""
WSGI config for fine_wine_n_dine project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fine_wine_n_dine.settings')

application = get_wsgi_application()
