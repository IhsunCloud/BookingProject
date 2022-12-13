from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):
    """
    Model definition of a country.

    Args:
        monetary_unit (str): monetary unit of country
        name (str): name of country
    """
    monetaryـunit  = models.CharField(
        _('Monetary Unit'),
        max_length = 64,
        help_text  = _('Monetary unit. e.g.: `Rial`'),
    )

    name = models.CharField(
        _('Country Name'),
        max_length = 64,
        help_text  = _('Name of the country. e.g.: `Iran`')
    )

    class Meta:
        """ Meta definition of country. """
        ordering = ('name',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        """ Unicode representation of country. """
        return f'{self.name} ~ {self.monetaryـunit}'

    def __repr__(self):
        """ Unicode representation of country. """
        return self.__str__()