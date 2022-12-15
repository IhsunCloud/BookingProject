from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    address = models.TextField(
        _('Address'),
    )

    city = models.TextField(
        _('City'),
        max_length = 16
    )

    country = models.CharField(
        _('Country'),
        max_length = 16
    )

    user = models.ForeignKey(
        'user.User',
        on_delete = models.CASCADE,
        related_name = 'users',
        verbose_name = _('User')
    )

    zip_code = models.CharField(
        _('Zip Code'),
        max_length = 16
    )


    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f'{self.user.username} ~ {self.user.phone_number}'