from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeFramedModel(models.Model):
    """
    An abstract base class model,
    That provides `start` & `end` fields to record a time-frame.
    """
    start = models.DateTimeField(_('start'), null=True, blank=True)
    end = models.DateTimeField(_('end'), null=True, blank=True)

    class Meta:
        abstract = True