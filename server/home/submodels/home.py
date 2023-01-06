from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.model_utils import upload_path
from painless.models import GeneralModel

from home.utils.choices import PropertyAmenities, HomeFeatures, HomeTypes


class Home(GeneralModel):
	"""
	Model definition of the Hotel.
	------------------------------

	Arguments:
	----------
		- GeneralModel (inherit):
		-------------------------
			- SluggedModel (str, slug): Slugged title.
			- TimeStampedModel (datetime): created_at, updated_at, deleted_at, trashed_at.

		- address (str): address of the hotel.
		- capacity (int): capacity of the hotel.
		- establishment_at (datetime): establishment date of the hotel.
		- name (str): name of the hotel.
		- home_class (float): rating of the hotel.
		- passenger (fk): passengers.
		- beds_number (int): number of beds.
		- entry_at (datetime): entry timestamp.
		- is_premium (bool): is the room is premium.
		- is_reserved (bool): is the room is reserved.
		- passenger (fk): passengers.
		- price (float): price of the room.
		- room_capacity (float): capacity of the room.
	"""
	address = models.CharField(
		_('Address'),
		max_length = 1000,
		help_text  = _('Address of the hotel. e.g: `126 Keshavarz Boulevard Sq Valiasr, Tehran, Iran.`')
	)

	description = models.TextField(
		_('Description')
	)

	home_class = models.FloatField(
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

	beds_number = models.SmallIntegerField(
		_('Beds Number'),
		help_text = _('Number of the beds. e.g: `2`')
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

	passenger = models.ForeignKey(
		'hotel.Passenger',
		on_delete = models.CASCADE,
		related_name = 'passengers',
		verbose_name = _('Passenger')
	)

	price = models.DecimalField(
    	_('Price'),
		decimal_places = 2,
		max_digits = 10,
		help_text  = _('Price of the room per days. e.g: `$1750`')
    )

	room_capacity = models.SmallIntegerField(
		_('Members Capacity'),
		help_text = _('Capacity of the room. e.g: `2`')
	)

	room_feature = ArrayField(
		_('Room Feature'),
		max_length = 3,
		choices = HomeFeatures.choices,
		blank   = True
	)

	room_number = models.IntegerField(
		_('Room Number'),
	)

	room_type = ArrayField(
		_('Room Type'),
		max_length = 3,
		choices    = HomeTypes.choices,
		blank 	   = True
	)

	class Meta:
		""" Meta definition of the Hotel. """
		ordering = ('name',)
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
		return f"NAME: {self.name}, 💫: CLS: {self.hotel_class}, DESC: {self.description}, ADDRESS: {self.address}"