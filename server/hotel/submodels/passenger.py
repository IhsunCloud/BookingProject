from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import SluggedModel, TimeStampedModel


class Passenger(SluggedModel, TimeStampedModel):
	"""
 	Model definition of Passenger.

	Args:
		SluggedModel (CharField, SlugField): contains title & slug
		TimeStampedModel (DateTime): contains timestamp filed

		adult: (fk): adult passengers
		members: (int) : member of passengers
	    underage: (fk): underage passengers
	"""
	adult = models.ForeignKey(
		'Adult',
		on_delete    = models.CASCADE,
		related_name = 'adults',
		verbose_name = _('Adult Passenger'),
	)

	adult = models.ForeignKey(
		'Underage',
		on_delete    = models.CASCADE,
		related_name = 'underages',
		verbose_name = _('Underages'),
	)

	class Meta:
		""" Meta definition of Passenger. """
		verbose_name = 'Passenger'
		verbose_name_plural = 'Passengers'


class Adult(TimeStampedModel):
    """
    Model definition of an adult passenger.
    """
    adult = models.ForeignKey(
		'user.User',
		on_delete    = models.CASCADE,
		related_name = 'adults',
		verbose_name = _('Adult'),
	)

    members = models.PositiveSmallIntegerField(
		_('Adult Members'),
        default = 0
	)


class Underage(TimeStampedModel):
    """
    Model definition of an underage passenger.
    """
    underages = models.ForeignKey(
		'user.User',
		on_delete    = models.CASCADE,
		related_name = 'underages',
		verbose_name = _('Underage'),
	)

    members = models.PositiveSmallIntegerField(
		_('Underage Members'),
        default = 0
	)

