from django.db import models
from django.utils.translation import gettext_lazy as _


class Phone(models.Model):
	"""
	Model definition of a phone number.
	"""
	hotel = models.ForeignKey(
		'hotel.Hotel',
		on_delete = models.CASCADE,
		related_name = 'hotels',
		verbose_name = _('Hotel')
	)

	number = models.CharField(
		_('Number'),
	 	max_length = 16
	)

	class Meta:
		""" Meta definition of the hotel. """
		ordering = ('hotel.name',)
		verbose_name = 'Phone'
		verbose_name_plural = 'Phones'

	def __str__(self):
		""" Unicode representation of the hotel. """
		return f'{self.hotel.name} ~ {self.number}'

	def __repr__(self):
		""" Unicode representation of the hotel. """
		return self.__str__()