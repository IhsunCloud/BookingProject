from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An AbstractBaseModel, that provides self-updating
    `created_at` & `modified_at` fields.
    """
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    class Meta:
        """
        Meta definition of TimeStampedModel.
        """
        abstract = True
        ordering = ('-created_at',)