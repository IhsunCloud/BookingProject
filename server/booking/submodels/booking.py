from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from painless import models as iModels

from .booking_status import BOOKING_STATUS

User = getattr(settings, 'AUTH_USER_MODEL', 'painless.User')


class Booking(iModels.GeneralModel):
    """
    Model definition of Booking.
    ----------------------------
    """
    booking_id = models.CharField(
        _('Booking ID'),
        max_length=128,
        help_text=_('Custom unique booking identifier.')
    )

    person = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # Change to SETNULL
        related_name='booking_persons',
        verbose_name=_('persons'),
    )

    booking_status = models.CharField(
        _('Booking Status'),
        max_length =16,
        choices = BOOKING_STATUS,
        default = BOOKING_STATUS[0],
        help_text=_('Current status of the booking. e.g.: Approved')
    )

    date_from = models.DateTimeField(
        verbose_name=_('From'),
        blank=True,
        null=True,
        help_text=_('From when the booking is active.')
    )

    date_until = models.DateTimeField(
        verbose_name=_('Until'),
        blank=True,
        null=True,
        help_text=_('Until when the booking is active.')
    )

    time_period = models.PositiveIntegerField(
        _('Time Period'),
        blank = True,
        null  = True,
        help_text = _('How long the period from date_from will be. e.g.: 10 (days).')
    )

    time_unit = models.CharField(
        _('Time Unit'),
        # default=getattr(settings, 'BOOKING_TIME_INTERVAL', ''),
        max_length = 64,
        blank = True,
        help_text = _('What unit of time the period is of. e.g.: nights or days.')
    )

    extra_persons = models.ForeignKey(
        User,
        related_name = 'extra_persons',
        verbose_name = _('Extra Persons'),
        on_delete = models.CASCADE, # Change to SETNULL
        null  = True,
        blank = True,
    )

    total = models.DecimalField(
        _('Total'),
        max_digits = 36,
        decimal_places = 2,
        blank = True,
        null  = True,
        help_text = _('Field for storing a total of all items.')
    )

    currency = models.CharField(
        _('Currency'),
        max_length = 128,
        blank = True,
        help_text = _('If total is uses, We usually also need a currency.')
    )

    class Meta:
        """ Meta information of Booking. """
        ordering = ['-created_at']
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

    def __str__(self):
        """ String representation of Booking. """
        return 'ID: {self.booking_id} ~ DATE: {self.created_at} ~ USER: {self.user}'

    def __repr__(self):
        """ String representation of Booking. """
        return self.__str__()

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super(Booking, self).save(*args, **kwargs)