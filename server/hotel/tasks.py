# in progress

from celery import shared_task

from django.db import transaction
from django.utils import timezone
from rest_framework import exceptions

from hotel import models


@shared_task
@transaction.atomic
def check_reservation():
    try:
        pass
    except Exception as e:
        raise exceptions.ValidationError("Error :{}".format(e))
    return True