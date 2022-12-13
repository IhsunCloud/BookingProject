from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    """
    Model definition of a image.
    """
    image = models.ImageField(
        _('Image'),
        upload_to = 'images/',
    )

    hotel = models.ForeignKey(
        'hotel.Hotel',
        on_delete = models.CASCADE,
        related_name = 'hotels',
        verbose_name = _('Hotel')
    )

    class Meta:
        """
        Meta definition of the image.
        """
        verbose_name = _('Image')
        verbose_name_plural = _('Image')