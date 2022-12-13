from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """
    Model definition of a city.

    Args:
        name (str): name of the city
        hotel (fk): the hotels of the city
        country (fk): name of the countries
        state (fk): name of the states
    """
    country = models.ForeignKey(
        'hotel.Country',
        on_delete = models.CASCADE,
        related_name = 'countries',
        verbose_name = _('Country'),
    )

    hotel = models.ForeignKey(
        'hotel.Hotel',
        on_delete = models.CASCADE,
        related_name = 'hotels',
        verbose_name = _('Hotel'),
    )

    name = models.CharField(
        _('Name'),
        max_length = 64,
        help_text = _('Name of the city. e.g: `Tehran`'),
    )

    state = models.ForeignKey(
        'hotel.State',
        on_delete = models.CASCADE,
        related_name = 'state',
        verbose_name = _('State'),
    )

    class Meta:
        """ Meta definition of city. """
        ordering = ('name',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        """ Unicode representation of city. """
        return f'{self.country.name} ~ {self.state.name} ~ {self.name}'

    def __repr__(self):
        """ Unicode representation of city. """
        return self.__str__()