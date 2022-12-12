from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import SluggedModel, TimeStampedModel


class BookingError(SluggedModel, TimeStampedModel):
    """
    Holds information about an error during a booking process.
    """
    booking = models.ForeignKey(
        'booking.Booking',
        on_delete=models.CASCADE,
        related_name='booking_errors',
        verbose_name=_('Booking'),
        help_text=_(' The booking during this error occurred.'),
    )
    
    message = models.CharField(
        _('Message'),
        max_length=1000,
        blank=True,
        help_text=_('The short error message, that you need to store.'),
    )
    
    details = models.TextField(
        _('Details'),
        max_length=4000,
        blank=True,
        help_text=_('A more in depth text about the error or any kind of additional information, e.g. a traceback.'),
    )
    
    class Meta:
        """ Meta definition of Booking ERROR. """
        ordering = ('-created_at',)
        verbose_name = _('ERROR')
        verbose_name_plural = _('ERRORS')

    def __str__(self):
        """ String representation of ERROR."""
        return 'DATE: {self.date} ~ ID: {self.booking.booking_id} ~ MSG: {self.message}'
    
    def __repr__(self):
        """ String representation of ERROR."""
        return self.__str__()