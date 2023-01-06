# import os

# from celery import Celery
# from celery.schedules import crontab

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kernel.settings.production')
# app = Celery()

# app.conf.timezone = 'ASIA/Tehran'

# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# app.conf.beat_schedule = {}