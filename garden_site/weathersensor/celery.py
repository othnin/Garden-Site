#celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garden_site.settings")
app = Celery("weathersensor")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



app.conf.beat_schedule = {
    'fetch-weather-every-day': {
        'task': 'weathersensor.tasks.fetch_and_save_weather',
        'schedule': crontab(hour=0, minute=0),  # Adjust the timing as needed
        #'schedule': crontab(),  #Every min to test
    },
}
app.conf.timezone = 'UTC'