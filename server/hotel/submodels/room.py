from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import SluggedModel, TimeStampedModel
from hotel.utils.choices import (
    PropertyAmenities,
    RoomFeatures,
    RoomTypes,
)


class Room(SluggedModel, TimeStampedModel):
	"""
	Model definition of a Room.

	Args:
		SluggedModel (str, slug): contains title & slug
		TimeStampedModel (datetime): contains timestamp filed

		passenger (fk): passengers
		beds_number (int): number of beds
		departure_at (datetime): departure timestamp
		entry_at (datetime): entry timestamp
		hotel (fk): hotel of the room
		is_premium (bool): is the room is premium
		is_reserved (bool): is the room is reserved
		passenger (fk): passengers
		price (float): price of the room
		room_capacity (float): capacity of the room
	"""
	beds_number = models.SmallIntegerField(
		_('Beds Number'),
		help_text = _('Number of the beds. e.g: `2`')
	)

	departure_at = models.DateField(
		_('Departure Date'),
		help_text = _('Departure Date. e.g: `2022-02-02`')
	)

	entry_at = models.DateField(
		_('Entry Date'),
		help_text = _('Departure Date. e.g: `2022-02-02`')
	)

	hotel = models.ForeignKey(
		'hotel.Hotel',
		on_delete = models.CASCADE,
		related_name = 'hotel_rooms',
		verbose_name = _('Hotel Room'),
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
		related_name = 'room_passengers',
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

	room_feature = models.CharField(
		_('Room Feature'),
		max_length = 3,
		choices = RoomFeatures.choices,
		blank   = True,
	)

	room_number = models.IntegerField(
		_('Room Number'),
	)

	room_type = models.CharField(
		_('Room Type'),
		max_length = 3,
		choices    = RoomTypes.choices,
		blank 	   = True
	)



