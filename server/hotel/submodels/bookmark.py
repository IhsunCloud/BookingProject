from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimeStampedModel


class Bookmark(TimeStampedModel):
    """AI is creating summary for Bookmark

    Args:
        TimeStampedModel (fk): timestamped

        user (fk): user belongs the bookmark
        hotel (fk): hotel belongs the bookmark
    """
    user = models.ForeignKey(
        'user.User',
        on_delete    = models.CASCADE,
        related_name = 'users',
        verbose_name = _('User')
    )

    hotel = models.ForeignKey(
        'hotel.Hotel',
        on_delete    = models.CASCADE,
        related_name = 'hotels',
        verbose_name = _('Hotel')
    )

    class Meta:
        """ Meta definition of the bookmark. """
        ordering = ('user', 'hotel',)
        verbose_name = _('Bookmark')
        verbose_name_plural = _('Bookmarks')

    def __str__(self):
        """ Unicode representation of the bookmark. """
        return f'{self.user.username} ~ {self.hotel.name}'

    def __repr__(self):
        """ Unicode representation of the bookmark. """
        return self.__str__()