from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Bookmark(iModels.TimeStampedModel):
    """
    Model definition of a Bookmark.
    -------------------------------

    Arguments:
    ----------
        - TimeStampedModel (fk):
          ----------------------
            - created_at
            - modified_at
            - trashed_at
            - deleted_at
        - user (fk):
          ----------
            user belongs to this bookmark.
        - hotel (fk):
          -----------
            hotel belongs to this bookmark.
    """

    home = models.ForeignKey(
        'home.Home',
        on_delete    = models.CASCADE,
        related_name = 'homes',
        verbose_name = _('Home')
    )

    class Meta:
        """ Meta definition of the bookmark. """
        verbose_name = _('Bookmark')
        verbose_name_plural = _('Bookmarks')

    def __str__(self):
        """ Unicode representation of the bookmark. """
        return f'{self.user.username} ~ {self.home.name}'

    def __repr__(self):
        """ Unicode representation of the bookmark. """
        return self.__str__()