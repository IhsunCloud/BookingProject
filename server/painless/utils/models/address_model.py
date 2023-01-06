from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressModel(models.Model):
    """
    Model definition of Address.

    Args:
        - city (fk):
            The city of the address.
        - country (fk):
            The country of the address.
        - zip_code (str):
            The zipcode of the address.
    """
    city = models.TextField(
        _('City'),
        max_length = 16
    )

    country = models.CharField(
        _('Country'),
        max_length = 16
    )

    zip_code = models.CharField(
        _('Zip Code'),
        max_length = 16
    )

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f'COUNTRY: {self.country} ~ CITY: {self.city} ~ ADDR: {self.address}'

    def __repr__(self):
        return self.__str__()


class Address(models.Model):
    """
    Model definition of Address.
    """
    address = models.TextField(
        _('Address'),
    )

    address_model = models.ForeignKey(
        AddressModel,
        on_delete = models.CASCADE,
        related_name = 'address',
        verbose_name = _('Address')
    )

    def __str__(self):
        return f'Address: {self.address}'

    def __repr__(self):
        return self.__str__()
