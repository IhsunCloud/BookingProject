from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimeStampedModel


class ExtraPersonInfo(TimeStampedModel):
    """
    Model definition of extra persons info.
    """
    special_request = models.TextField(
        _('Special Request'),
        max_length=1024,
        blank=True,
    )

    notes = models.TextField(
        _('Notes'),
        max_length=1024,
        blank=True,
    )
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Extra persons Info')
        verbose_name_plural = _("Extra Persons Info")