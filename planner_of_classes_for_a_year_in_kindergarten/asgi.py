"""
ASGI config for planner_of_classes_for_a_year_in_kindergarten project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planner_of_classes_for_a_year_in_kindergarten.settings')

application = get_asgi_application()
