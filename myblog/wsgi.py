"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('BLOG_PROFIEL', 'develop')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"myblog.settings.{profile}")

application = get_wsgi_application()
