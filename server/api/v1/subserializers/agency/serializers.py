from rest_framework import serializers

from agency.models import Agency, PhoneNumber
from painless.models import AddressModel

from ..booking.serializers import BookingSerializer
from ..user.serializers import UserSerializer


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
      model  = PhoneNumber
      fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel


class AgencySerializer(serializers.ModelSerializer):
    booking = BookingSerializer()
    user  = UserSerializer()
    phone = PhoneNumberSerializer()

    class Meta:
      model  = Agency
      fields = '__all__'