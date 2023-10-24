"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
import threading
from email_distribution.scheduler import check_scheduler, scheduler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Запуск планировщика перед запуском приложения Django
check_thread = threading.Thread(target=check_scheduler)
scheduler.start()

# Получение объекта приложения WSGI
application = get_wsgi_application()
