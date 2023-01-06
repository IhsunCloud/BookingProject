from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Bus(models.Model):
    """
    Model definition of Bus.
    ------------------------

    Arguments:
    ----------
        - driver (fk):
          ------------
            -> driver of the bus
        - seat_number:
          ------------
            -> number of bus seats
    """
    driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'drivers',
        verbose_name = _('Driver'),
    )

    seats_number = models.IntegerField(
        _('Seats Number'),
        default=24,
    )


class BusReservation(iModels.GeneralModel):
    """
    Model definition of Bus Reservation.
    ------------------------------------

    Arguments:
    ----------
        #TODO: in progress ..
    """
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete = models.CASCADE,
        related_name = 'agencies',
        verbose_name = _('Agency')
    )

    booking = models.ForeignKey(
        'booking.Booking',
        on_delete = models.CASCADE,
        related_name = 'bus_bookings',
        verbose_name = _('Booking')
    )

    bus = models.ForeignKey(
        'bus.Bus',
        on_delete = models.CASCADE,
        related_name = 'bus',
        verbose_name = _('Bus')
    )

    passenger = models.ForeignKey(
        'bus.Passenger',
        on_delete = models.CASCADE,
        related_name = 'passengers',
        verbose_name = _('Passenger')
    )

    time_to_go = models.DateTimeField(
        _('Time to go'),
        auto_now_add = True
    )

    is_reserved = models.BooleanField(
        _('Is Reserved'),
        default = False
    )

    seat_number = models.IntegerField(
        _('Seat Number'),
        default = 24
    )

    class Meta:
        """ Meta definition of Bus Reservation. """
        ordering = ('seat_number',)
        verbose_name = _('Bus Reservation')
        verbose_name_plural = _('Bus Reservations')

    def __str__(self):
        """ Unicode representation of the BusReservation. """
        return f"PASSENGER: {self.passenger} | (SEAT NO: {self.seat_number}) ~ AGENCY: {self.agency} ~ DEPARTURE_TIME: {self.time_to_go}"

    def __repr__(self):
        """ Unicode representation of the BusReservation. """
        return self.__str__()