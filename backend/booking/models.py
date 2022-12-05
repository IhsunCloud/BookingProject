from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import GeneralModel
from painless.models import TimeStampedModel


class Booking(GeneralModel, TimeStampedModel):
    """
    Model definition of Booking.
    """
    pass
    