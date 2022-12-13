from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import (
	SluggedModel,
	TimeStampedModel
)
from hotel.choices import PropertyAmenities


class Hotel(SluggedModel, TimeStampedModel):
	"""
	Model definition of the hotel.

	Args:
		SluggedModel (str, slug): Slugged title
		TimeStampedModel (datetime): Timestamped

		address (str): address of the hotel
		capacity (int): capacity of the hotel
		establishment_at (datetime): establishment date of the hotel
		name (str): name of the hotel
		hotel_class (float): rating of the hotel
	"""
	address = models.CharField(
		_('Address'),
		max_length = 1000,
		help_text  = _('Address of the hotel. e.g: `126 Keshavarz Boulevard Sq Valiasr, Tehran, Iran.`')
	)

	capacity = models.IntegerField(
		_('Capacity'),
		help_text = _('Capacity of the hotel. e.g: `150`')
	)

	descriptor = models.TextField(
		_('Description')
	)

	establishment_at = models.DateField(
		_('Establishment Date'),
		help_text = _('Establishment date. e.g: `2015-01-01')
	)

	logo = models.ImageField(
		_('Image'),
		upload_to = 'hotel/logo/',
		blank = True
	)

	name = models.CharField(
		_('Name'),
		max_length = 128,
		help_text  = _('Name of the hotel. e.g. `Espinas International Hotel, At The Boulevard`')
	)

	hotel_class = models.FloatField(
		_('Rating of the hotel'),
		help_text = _('Rating of the hotel. e.g: `5')
	)
 
	property_amenities = models.CharField(
		_('Property Amenities'),
		choices = PropertyAmenities.choices,
		blank   = True
    )

	class Meta:
		""" Meta definition of the Hotel. """
		ordering = ('name', '-hotel_class',)
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotels'

	def __str__(self):
		""" Unicode representation of the hotel. """
		return f'{self.name} ~ {self.hotel_class}'

	def __repr__(self):
		""" Unicode representation of the hotel. """
		return self.__str__()