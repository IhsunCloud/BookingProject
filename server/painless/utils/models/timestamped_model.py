from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.managers import SoftDeletableManager
from .trashable_model import TrashableModel


class TimeStampedModel(TrashableModel):
    """
    Model definition of the TimeStamped.

    An AbstractBaseModel, that provides self-updating:
        - created_at
        - deleted_at
        - modified_at
        - trashed_at
    """
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    # manager    = SoftDeletableManager()

    class Meta:
        """ Meta definition of TimeStampedModel. """
        abstract = True
        ordering = ('-created_at',)