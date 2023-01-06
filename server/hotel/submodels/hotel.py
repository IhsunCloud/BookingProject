from django.db import models
from django.utils.translation import gettext_lazy as _

from painless import models as iModels
from painless.model_utils import upload_path

from hotel.utils.choices import PropertyAmenities


class Hotel(iModels.GeneralModel):
	"""
	Model definition of the Hotel.

	GeneralModel:
		- title (str): title of the model.
		- slug  (str): title slugify.
		- timestamped (datetime):
			- created_at
			- updated_at
			- trashed_at
			- deleted_at
	Arguments:
		- address (str):
  			address of the hotel.
		- capacity (int):
			capacity of the hotel.
		- establishment_at (datetime):
			establishment date of the hotel.
		- logo (image):
			logo of the hotel.
		- name (str):
			name of the hotel.
		- hotel_class (float):
			rating of the hotel.
		- property_amenities (choice):
			property amenities of the hotel.
		- rooms_number (int):
			number of the rooms.
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

	description = models.TextField(
		_('Description')
	)

	establishment_at = models.DateField(
		_('Establishment Date'),
		help_text = _('Establishment date. e.g: `2015-01-01')
	)

	entry_at = models.DateField(
		_('Entry Date'),
		help_text = _('Departure Date. e.g: `2022-02-02`')
	)

	is_premium = models.BooleanField(
		_('Is Premium'),
		default   = False,
		help_text = _('Is this room is premium? e.g: `False`')
	)

	is_reserved = models.BooleanField(
		_('Is Reserved'),
		default   = False,
		help_text = _('Is this room is reserved? e.g: `False')
	)

	hotel_class = models.FloatField(
		_('Rating of the hotel'),
		help_text = _('Rating of the hotel. e.g: `5')
	)

	logo = models.ImageField(
		_('Logo'),
		upload_to = upload_path,
		blank = True
	)

	name = models.CharField(
		_('Name'),
		max_length = 128,
		help_text  = _('Name of the hotel. e.g. `Espinas International Hotel, At The Boulevard`')
	)

	property_amenities = models.CharField(
		_('Property Amenities'),
		max_length = 128,
		choices = PropertyAmenities.choices,
		blank   = True
	)

	rooms_number = models.IntegerField(
		_('Number of Rooms')
	)

	class Meta:
		""" Meta definition of the Hotel. """
		ordering = ('name', '-hotel_class',)
		verbose_name = _('Hotel')
		verbose_name_plural = _('Hotels')

	def __str__(self):
		""" Unicode representation of the hotel. """
		return f'{self.name} ~ {self.hotel_class}'

	def __repr__(self):
		""" Unicode representation of the hotel. """
		return self.__str__()

	@property
	def descriptor(self):
		""" The descriptor of the hotel. """
		return f"NAME: {self.name}, CLS: {self.hotel_class}, DESC: {self.description}, ADDRESS: {self.address}"