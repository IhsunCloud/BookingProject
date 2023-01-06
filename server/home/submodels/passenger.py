from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels

User = getattr(settings, 'AUTH_USER_MODEL', 'painless.User')


class Passenger(iModels.GeneralModel):
	"""
 	Model definition of Passenger.
	------------------------------

	Arguments:
	----------
		- SluggedModel (str):
			-> contains title & slug
		- TimeStampedModel (datetime):
			-> contains timestamp filed
		- adult: (fk):
			-> adult passengers
		- members: (int) :
			-> member of passengers
	    - underage: (fk):
			-> underage passengers
	"""
	adult = models.ForeignKey(
		'Adult',
		on_delete    = models.CASCADE,
		related_name = 'adult_passengers',
		verbose_name = _('Adult Passenger'),
	)

	underage = models.ForeignKey(
		'Underage',
		on_delete    = models.CASCADE,
		related_name = 'underage_passengers',
		verbose_name = _('Underages'),
		null = True
	)

	class Meta:
		""" Meta definition of Passenger. """
		verbose_name = 'Passenger'
		verbose_name_plural = 'Passengers'


class Adult(iModels.TimeStampedModel):
    """
    Model definition of an adult passenger.
    """
    adult = models.ForeignKey(
		User,
		on_delete    = models.CASCADE,
		related_name = 'adult_passengers',
		verbose_name = _('Adult'),
	)

    members = models.PositiveSmallIntegerField(
		_('Adult Members'),
        default = 0
	)


class Underage(iModels.TimeStampedModel):
    """
    Model definition of an underage passenger.
    """
    underages = models.ForeignKey(
		User,
		on_delete    = models.CASCADE,
		related_name = 'underage_passengers',
		verbose_name = _('Underage'),
	)

    members = models.PositiveSmallIntegerField(
		_('Underage Members'),
        default = 0
	)

