"""
NPUSPTA asgi.py file not required, only in term of asynchronous web server
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
