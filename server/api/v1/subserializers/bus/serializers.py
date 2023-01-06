from rest_framework import serializers

from bus import models

from ..agency.serializers import AgencySerializer
from ..booking.serializers import BookingSerializer
from ..user.serializers import UserSerializer


class BusSerializer(serializers.ModelSerializer):
	driver = UserSerializer()

	class Meta:
		model  = models.Bus
		fields = '__all__'


class AdultSerializer(serializers.ModelSerializer):
	class Meta:
		model  = models.Adult
		fields = '__all__'


class UnderageSerializer(serializers.ModelSerializer):
	class Meta:
		model  = models.Underage
		fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
	adult = AdultSerializer()
	underage = UnderageSerializer()

	class Meta:
		model  = models.Passenger
		fields = '__all__'

class BusReservationSerializer(serializers.ModelSerializer):
	bus = BusSerializer()
	agency  = AgencySerializer()
	booking = BookingSerializer()
	passenger = PassengerSerializer()

	class Meta:
		model  = models.BusReservation
		fields = '__all__'