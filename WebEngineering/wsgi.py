"""
WSGI config for WebEngineering project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys
root_path= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0,root_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebEngineering.settings')

application = get_wsgi_application()
