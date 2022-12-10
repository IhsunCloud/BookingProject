from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)


class TimeStampedModel(models.Model):
    """
    An AbstractBaseModel, that provides self-updating
    `created_at` & `modified_at` fields.
    """
    created_at = AutoCreatedField(_('Created At'), auto_now_add=True)
    updated_at = AutoLastModifiedField(_('Updated At'), auto_now=True)
    class Meta:
        """
        Meta definition of TimeStampedModel.
        """
        abstract = True
        ordering = ('created_at',)
    
    def save(self, *args, **kwargs):
        """
        Make sure that modified field is updated even,
        if it is not given as a parameter to the update field argument.
        """
        update_fields = kwargs.get('update_fields', None)
        
        if update_fields:
            kwargs['update_fields'] = set(update_fields).union({'modified_at'})
            
        super().save(*args, **kwargs)