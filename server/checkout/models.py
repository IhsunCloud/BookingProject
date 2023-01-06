import holidays

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
	price = models.ForeignKey(
		'Price',
		on_delete = models.CASCADE,
		related_name = 'price',
		verbose_name = _('Price')
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

	def add_discount(self, country, subdiv):
		us_holidays = holidays.country_holidays(country='US', subdiv='PR')
		if self.order.created_at in us_holidays:
			has_discounts = True
			# add some logic ...
			pass


class Currency(models.Model):
	"""
	Model definition of the Currency.
	"""
	name = models.CharField(
		_('Name'),
		max_length = 64
	)

	code = models.CharField(
		_('Code'),
		max_length = 4
	)

	def __str__(self):
		return f'{self.name} ~ {self.code}'


class Price(models.Model):
	"""
	Model definition of the Price.
	"""
	value = models.FloatField(
		_('Value'),
		default=0.0
	)

	from_date = models.DateField(
		_('From Date'),
		null  = True,
		blank = True
	)

	to_date = models.DateField(
		_('To Date'),
		null  = True,
		blank = True
	)

	ratio = models.FloatField(
		_('Ratio'),
		default = 0.0
	)

	currency = models.ForeignKey(
		_('Currency'),
		Currency,
		on_delete    = models.CASCADE,
		related_name = 'currency'
	)

	def __str__(self):
		""" String representation of the Price. """
		return '{} ({})'.format(str(self.value), self.currency.code)

	def __repr__(self) -> str:
		""" String representation of the Price. """
		return super().__repr__()


class CurrencyExchangeRate(models.Model):
	"""
	Model definition of the Currency Exchange Rate.
	"""
	rate = models.FloatField(
		_('Rate'),
	)

	currency_from = models.ForeignKey(
		'Currency',
		verbose_name = _('Currency From'),
		on_delete = models.CASCADE,
		related_name = "currency_from"
	)

	currency_to = models.ForeignKey(
		'Currency',
		verbose_name = _('Currency to'),
		on_delete    = models.CASCADE,
		related_name = "currency_to"
	)

	def __str__(self):
		""" String representation of the Currency Exchange Rate. """
		return "{}/{}: {}".format(self.currency_from.code, self.currency_to.code, str(self.rate))

	def __repr__(self) -> str:
		""" String representation of the Currency Exchange Rate. """
		return super().__repr__()