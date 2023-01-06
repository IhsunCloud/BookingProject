from django.db import models
from django.utils.translation import gettext_lazy as _


class Airplane(models.Model):
    """
    Model definition of the Airplane.
    ---------------------------------

    Arguments:
    ----------
        - agency (fk):
          ------------
            -> the agency associated
        - pilot (str):
          ------------
            -> the pilot associated
        - source (fk):
          ------------
            -> the source associated
        - destination (fk):
          -----------------
            -> the destination associated
    """
    agency = models.ForeignKey(
        'agency.Agency',
        on_delete = models.CASCADE,
        related_name = 'airplane',
        verbose_name = _('Agency')
    )

    pilot  = models.CharField(
        _('Pilot'),
        max_length = 128
    )

    source = models.ForeignKey(
        'airport.Airport',
        on_delete=models.CASCADE,
        related_name='source',
        verbose_name = _('The source associated')
    )

    destination = models.ForeignKey(
        'airport.Airport',
        on_delete = models.CASCADE,
        related_name = 'destination',
        verbose_name = _('The destination associated')
    )


    def __str__(self):
        pass

    def save(self):
        pass

    class Meta:
        pass