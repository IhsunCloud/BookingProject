from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Agency(iModels.GeneralModel):
    """
    Model definition of the Agency.
    -------------------------------

    Arguments:
    ----------
        - GeneralModel (iModels):
          -----------------------
            -> title, slug, yusef_id, created_at, updated_at, deleted_at, trashed_at
        - user (fk):
          ----------
            -> that admins of this Agency.
        - booking (fk):
          -------------
            -> the booking that belongs to this Agency.
        - phone (PhoneNumberField):
          -------------------------
            -> phone number of this Agency.
        - city (fk):
          ----------
            -> the city of the Agency.
        - address (fk):
          -------------
            -> the address of the Agency.
        - airport (fk):
          -------------
            -> the Airports of this Agency.
    """
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete = models.CASCADE,
      verbose_name = _('User'),
      related_name = _('agency_users'),
    )

    phone = models.ForeignKey(
      'PhoneNumber',
      on_delete = models.CASCADE,
      related_name = _('agency_phone_number'),
      verbose_name = _('Phone Number'),
    )

    address = iModels.AddressModel(
      _('Address')
    )

    booking = models.ForeignKey(
        'booking.Booking',
        on_delete = models.CASCADE,
        related_name = "agency_booking",
        verbose_name = _("agency_booking")
    )

    airport = models.ForeignKey(
      'airport.Airport',
      on_delete = models.CASCADE,
      related_name = "agency_airport",
      verbose_name = _("Agency Airport")
    )


    def __str__(self):
        """ String representation of the Agency. """
        return f"{self.name} ~ {self.address}"

    def __repr__(self):
        """ String representation of the Agency. """
        return self.__str__()


class PhoneNumber(models.Model):
    """ Model definition of the Phone. """
    phone = models.CharField(_('Phone Number'), max_length=16)