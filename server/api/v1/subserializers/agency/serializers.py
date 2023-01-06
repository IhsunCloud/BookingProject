from rest_framework import serializers

from agency.models import Agency, PhoneNumber
from booking.models import Booking
from painless.models import AddressModel, User

from ..booking.serializers import BookingSerializer
from ..user.serializers import UserSerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
      model  = PhoneNumber
      fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AddressModel
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    booking = BookingSerializer(many=True)
    phone = PhoneNumberSerializer(many=True)
    user  = UserSerializer(many=True)

    class Meta:
      model  = Agency
      fields = '__all__'