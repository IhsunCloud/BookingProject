from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimeStampedModel


class ExtraPersonInfo(TimeStampedModel):
    """
    Model definition of extra persons info.
    ---------------------------------------

    Arguments:
    ----------
        - TimeStampedModel (fk):
          ----------------------
            -> created_at, updated_at, deleted_at, trashed_at
        - special_request (str):
          ----------------------
            -> user can order a special request.
        - notes (str):
          ------------
            -> user can add a note.
    """
    booking = models.ForeignKey(
        'booking.ExtraPersonInfo',
        on_delete = models.CASCADE, # Change to SETNULL
        related_name = 'user_extra_person_info',
        blank = True,
        help_text = _('Extra Info, including note or special request.')
    )

    special_request = models.TextField(
        _('Special Request'),
        max_length = 1024,
        blank = True,
    )

    notes = models.TextField(
        _('Notes'),
        max_length = 1024,
        blank = True,
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Extra persons Info')
        verbose_name_plural = _("Extra Persons Info")