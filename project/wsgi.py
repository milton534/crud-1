"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
activate_this = '/home/matsuzawa505/.virtualenvs/django16/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this)

import os
import sys

path = '/home/matsuzawa505/project'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django.core.handlers.wsgi
# application = get_wsgi_application()
application = django.core.handlers.wsgi.WSGIHandler()
