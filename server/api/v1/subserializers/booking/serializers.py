from rest_framework import serializers
from booking import models

from ..user.serializers import UserSerializer


class BookingErrorSerializer(serializers.ModelSerializer):
	# booking = BookingSerializer(many=True)

	class Meta:
		model  = models.BookingError
		fields = '__all__'


class BookingItemSerializer(serializers.ModelSerializer):
	# booking = BookingSerializer(many=True)

	class Meta:
		model  = models.BookingItem
		fields = '__all__'


class ExtraPersonInfoSerializer(serializers.ModelSerializer):
	# booking = BookingSerializer(many=True)

	class Meta:
		model  = models.ExtraPersonInfo
		fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
	person = UserSerializer(many=True)
	extra_persons = UserSerializer(many=True)
	booking_error = BookingErrorSerializer(many=True)
	booking_item  = BookingItemSerializer(many=True)
	extra_person_info = ExtraPersonInfoSerializer(many=True)

	class Meta:
		model = models.Booking
		fields = '__all__'