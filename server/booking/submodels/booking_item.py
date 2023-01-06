from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class BookingItem(iModels.GenericModel):
    """
    Model to connect a booking with a related object.
    """
    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=1,
    )

    persons = models.PositiveIntegerField(
        _('Persons'),
        null = True,
        blank = True,
        help_text = _('Quantity of persons, who are involved in this booking.'),
    )

    subtotal = models.DecimalField(
        _('Subtotal'),
        max_digits=36,
        decimal_places = 2,
        null = True,
        blank = True,
        help_text = _('Field for storing the price of each individual item.'),
    )

    booking = models.ForeignKey(
        'booking.Booking',
        on_delete = models.CASCADE,
        related_name = 'bookings',
        verbose_name = _('Booking'),
        help_text = _('Connection to related booking.'),
    )

    class Meta:
        """ Meta definition of Booking. """
        ordering = ['-booking__created_at']

    def __str__(self):
        """ String representation of Booking. """
        return f'{self.booking}, {self.booked_item}'

    def __repr__(self):
        """ String representation of Booking. """
        return self.__str__()