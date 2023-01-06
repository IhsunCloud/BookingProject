from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Airport(iModels.GeneralModel):
    """
    Model definition of the Airport.
    --------------------------------

    Arguments:
    ----------
        - GeneralModel (iModels):
          -----------------------
            -> title, slug, yusef_id, created_at, updated_at, deleted_at, trashed_at
        - address (iModels):
          ------------------
            -> city, country, zip_code
        - phone (fk):
          -----------
            -> the phone numbers of this airport.
    """
    address = iModels.AddressModel(
        _('Address of the Airport'),
    )


class PhoneNumber(iModels.TimeStampedModel):
    """ Model definition of the Phone. """
    phone  = models.CharField(
        _('Phone Number'),
        max_length=16
    )

    airport = models.ForeignKey(
        'airport.Airport',
        on_delete = models.CASCADE,
        related_name = 'airport_phone_number',
        verbose_name = _('Airport'),
        null = True
    )