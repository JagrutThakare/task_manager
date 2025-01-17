from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

# Enable broker connection retry on startup
broker_connection_retry_on_startup = True

app = Celery('task_manager')

# Load settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Update timezone settings
app.conf.update(
    timezone='Asia/Kolkata',  # Set your desired time zone
    enable_utc=True,          # Enable UTC for internal consistency
)

# Discover tasks in registered Django apps
app.autodiscover_tasks()
