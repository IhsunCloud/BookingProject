import math
from django.db.models.signals import post_save
from django.dispatch import receiver

from cart.models import OrderItem


@receiver(post_save, sender = OrderItem)
def cart_update_price(sender, instance, **kwargs):
    if instance.booking.has_discount:
        # total = math.fsum(instance.price * instance.quantity for instance in instance.booking.all)    
        instance.price = instance.price - (instance.price * instance.booking.discount / 100)
        instance.save()
