"""
WSGI config for exampleproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exampleproject.settings")

if settings.USE_SENTRY:
    application = Sentry(get_wsgi_application())
else:
    application = get_wsgi_application()
