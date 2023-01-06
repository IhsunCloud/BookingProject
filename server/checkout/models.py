from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.utils.models.timestamped_model import TimeStampedModel


class Order(models.Model):
	"""
 	Model definition for Orders.
  	"""
	customer = models.ForeignKey(
		'painless.Profile',
  		related_name = "orders",
		verbose_name = _('Customer'),
		on_delete = models.CASCADE,
		null = True
	)

	class Meta:
		""" Meta information of Order. """
		verbose_name = _('Order')
		verbose_name_plural = _('Orders')

	def __str__(self):
		""" Unicode representation of Orders. """
		return  self.customer.__str__

	def __repr__(self):
		""" Unicode representation of Orders. """
		return  self.customer.__str__


class OrderItem(TimeStampedModel):
	"""
 	Model definition for Cart Items.
  	"""
	order = models.ForeignKey(
	 	'checkout.Order',
	  	verbose_name = _('Order'),
		related_name = 'items',
		on_delete = models.CASCADE,
  		null = True
	)

	booking = models.ForeignKey(
	 	'booking.Booking',
	  	related_name = 'booking',
	   	verbose_name = _('Booking'),
		on_delete    = models.CASCADE, 
  		null = True
	)

	quantity = models.IntegerField(
	 _('Quantity'),
	)

	class Meta:
		""" Meta information of Order Item. """
		ordering = ('-created_at',)
		verbose_name = _('Order Item')
		verbose_name_plural = _('Order Items')

	def __str__(self):
		""" Unicode representation of Order Items. """
		return f'{self.booking.title} + {self.price}'

	def __repr__(self):
		""" Unicode representation of Order Items. """
		return self.__str__()


class PriceBooking(TimeStampedModel):
	price = models.DecimalField(
	 	_("Price"),
	  	max_digits = 10,
	   	decimal_places = 0,
	)

	order = models.ForeignKey(
		'checkout.OrderItem',
		on_delete = models.CASCADE,
		related_name = 'booking_price',
		verbose_name = _('Order Item')
	)

	has_discounts = models.BooleanField(
     _('Discount'),
     default = False
	)

	discount = models.DecimalField(
    	_('Discount'),
		max_digits = 5,
		decimal_places = 2
	)