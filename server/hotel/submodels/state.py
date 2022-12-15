from django.db import models
from django.utils.translation import gettext_lazy as _


class State(models.Model):
    """
    Model definition of a state.

    Args:
        name (str): name of the state
        country (fk): country of the state
    """
    name = models.CharField(
        _('Name'),
        max_length = 64
    )

    country = models.ForeignKey(
        'hotel.Country',
        on_delete = models.CASCADE,
        related_name = 'countries',
        verbose_name = 'Country',
    )