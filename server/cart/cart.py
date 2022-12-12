from decimal import Decimal
from django.conf import settings

from booking.models import Booking


class Cart(object):
    """
    Initialize the Cart.
    """
    def __init__(self, request, *args, **kwargs):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            self.session[settings.CART_SESSION_ID] = {}
            cart = self.session[settings.CART_SESSION_ID]
        self.cart = cart

    def add(self, booking, quantity = 1, update_count = False):
        booking_id = str(booking.id)
        
        if booking_id not in self.cart:
            self.cart[booking_id] = {
                'quantity': 0, 
                'price': str(booking.price)
            }
        if update_count:
            self.cart[booking_id]['quantity'] = quantity
        else:
            self.cart[booking_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, booking):
        booking_id = str(booking)
        
        if booking_id in self.cart:
            del self.cart[booking_id]
            self.save()
    
    def __iter__(self):
        booking_ids = self.cart.keys()
        bookings = Booking.objects.filter(id__in = booking_ids)
        
        for booking in bookings:
            self.cart[str(booking.id)]['product'] = booking
    
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['booking_count']
            yield item

    def __len__(self):
        return sum(item['booking_count'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Int(item['price']) * item['booking_count'] for item in self.cart.values())
    
    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True