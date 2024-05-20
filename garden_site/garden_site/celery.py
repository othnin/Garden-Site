#celery.py
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "garden_site.settings")
app = Celery("garden_site")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()