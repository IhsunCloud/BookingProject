from django.db import models
from django.utils.translation import ugettext_lazy as _

from .trashable_mixins.mixins import NonTrashedManager
from .trashable_mixins.mixins import TrashedManager

try:
    from django.utils import timezone as datetime
except ImportError:
    from datetime import datetime
    

class TrashableModel(models.Model):
    """
    An abstract base class model,
    which allow objects to be "trashed" before finally deleted.
    """
    
    trashed_at = models.DateTimeField(
        _('Trashed'),
        editable = False,
        blank = True,
        null  = True
    )

    objects = NonTrashedManager()
    trash = TrashedManager()

    class Meta:
        """ Meta definition of Trashable Model. """
        abstract = True
        ordering = ('-trashed_at',)
        verbose_name = _('Trashable Model')
        verbose_name_plural = _('Trashable Models')
        
    def delete(self, *args, **kwargs):
        trash = kwargs.get('trash', True)
        
        if not self.trashed_at and trash:
            self.trashed_at = datetime.now()
            self.save()
        super(TrashableModel, self).delete(*args, **kwargs)

    def restore(self, commit=True):
        self.trashed_at = None
        if commit:
            self.save()
            