from rest_framework import serializers

from checkout import models

from ..booking.serializers import BookingSerializer
from ..user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
	customer = UserSerializer()

	class Meta:
		model  = models.Order
		fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
	booking = BookingSerializer()
	order   = OrderSerializer()

	class Meta:
		model  = models.OrderItem
		fields = '__all__'


class PriceBookingSerializer(serializers.ModelSerializer):
	order = OrderSerializer()

	class Meta:
		model  = models.PriceBooking
		fields = '__all__'