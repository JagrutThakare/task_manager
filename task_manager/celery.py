from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

broker_connection_retry_on_startup = True

app = Celery('task_manager')

# Load settings from Django's settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Update timezone settings
app.conf.update(
    timezone='Asia/Kolkata',  # Set your desired time zone
    enable_utc=False,          # Enable UTC for internal consistency
)


# Celery Beat Settings

app.conf.beat_schedule = {
    'generate_weekly_reports': {
        'task': 'task_manager.tasks.generate_weekly_reports',
        'schedule': crontab(hour=9, minute=00, day_of_week=1),  # Every Monday at 9:00 AM
    },
    'generate_reports': {
        'task': 'task_manager.tasks.generate_reports',
        'schedule': crontab(hour=16, minute=10, day_of_week='1'),
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    


