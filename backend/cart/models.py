from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
	"""
 	Model definition for Orders.
  	"""
	customer = models.ForeignKey(
		'user.User',
  		related_name = "orders",
		verbose_name = _('Customer'),
		on_delete = models.CASCADE,
		null = True
	)
 
	class Meta:
		""" Meta information of Order. """
		ordering = ('-created_at',)
		verbose_name = _('Order')
		verbose_name_plural = _('Orders')

	def __str__(self):
		""" Unicode representation of Orders. """
		return  self.customer.fullname
	
	def __repr__(self):
		""" Unicode representation of Orders. """
		return self.__str__()


class OrderItem(TimeStampedModel):
	"""
 	Model definition for Cart Items.
  	"""
	order = models.ForeignKey(
	 	'cart.Order',
	  	verbose_name = _('Order'),
		related_name = 'items',
		on_delete = models.CASCADE,
  		null = True
	)
 
	booking = models.ForeignKey(
	 	'cart.Booking',
	  	related_name = 'order_items',
	   	verbose_name = _('Booking'),
		on_delete    = models.CASCADE, 
  		null = True
	)
 
	price = models.DecimalField(
	 	_("Price"),
	  	max_digits = 10,
	   	decimal_places = 0,
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
		return f'{self.products.title} + {self.price}'

	def __repr__(self):
		""" Unicode representation of Order Items. """
		return self.__str__()