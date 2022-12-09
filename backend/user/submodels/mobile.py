from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimeStampedModel


class Mobile(TimeStampedModel):
    """
    Model definition of a mobile devices.
    """
    phone = models.CharField(
        _('Phone Number'),
        max_length = 16
    )
    
    persons = models.ForeignKey(
        'user.User',
        on_delete= models.CASCADE, # Change to SETNULL
        related_name='persons',
        verbose_name = _('Persons')
    )
    
    class Meta:
        """ Meta definition of a mobile device. """
        ordering = ('-created_at',)
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
        
    def __str__(self):
        """ String representation of mobile devices. """
        return "{self.phone} ~ {self.persons}"
    
    def __repr__(self):
        """ String representation of mobile devices. """
        return self.__str__()
    
    @property
    def generate_otp(self):
        pass