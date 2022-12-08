from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import GeneralModel, TimeStampedModel


class BookingStatus(GeneralModel, TimeStampedModel):
	"""
	Model definition of Booking Status.
	"""
	class BookingStatus(models.TextChoices):
		pass

	desc = models.TextField(
		_('Status Description'),
		blank=True
	)
	
	status = models.CharField(
		_('Booking Status'),
    	max_length=2,
    	choices=BookingStatus.choices
    )
