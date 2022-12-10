from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.fields import (
    MonitorField,
    StatusField,
)


class StatusModel(models.Model):
    """
    An abstract base class model with a ``status`` field that
    automatically uses a ``STATUS`` class attribute of choices, a
    ``status_changed`` date-time field that records when ``status``
    was last modified, and an automatically-added manager for each
    status that returns objects with that status only.
    """
    status = StatusField(_('status'))
    status_changed = MonitorField(_('status changed'), monitor='status')

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        status_changed field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get('update_fields', None)
        if update_fields and 'status' in update_fields:
            kwargs['update_fields'] = set(update_fields).union({'status_changed'})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True