from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Tour(iModels.GeneralModel):
    """
    Model definition of the Tour.
    -----------------------------

    Arguments:
    ----------
        GeneralModel:
        -------------
            - title: str
            - slug: str
            - timestamped: datetime
            - user: fk
            - us_id: fk
        - booking: fk
        - description: str
        - home: fk
        - hotel: fk
    """
    booking = models.ForeignKey(
        'booking.Booking',
        on_delete = models.CASCADE,
        related_name = 'Booking',
        verbose_name = _('Booking'),
    )

    description = models.TextField(
        _("Tour Descriptor")
    )

    hotel = models.ForeignKey(
        'hotel.Hotel',
        on_delete = models.CASCADE,
        related_name = 'hotel_tours',
        verbose_name = 'Hotel',
        blank = True
    )

    home  = models.ForeignKey(
        'home.Home',
        on_delete = models.CASCADE,
        related_name = 'home_tours',
        verbose_name = 'Home',
        blank = True
    )

    class Meta:
        """ Meta definition of the Tour. """
        ordering = ('-created_at',)

    def __str__(self):
        """ String representation of the Tour. """
        return self.title

    def __repr__(self):
        """ String representation of the Tour. """
        return self.__str__()