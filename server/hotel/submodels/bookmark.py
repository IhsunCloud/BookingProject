from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimeStampedModel
from painless.fields import UserField


class Bookmark(TimeStampedModel):
    """
    Model definition of a bookmark.

    Args:
        - TimeStampedModel (fk):
            timestamped
        - user (fk):
            user belongs the bookmark
        - hotel (fk):
            hotel belongs the bookmark
    """
    user = UserField()

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