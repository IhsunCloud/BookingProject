from rest_framework import serializers

from airport import models

from ..painless.serializers import AddressSerializer


class AirportSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model  = models.Airport
        fields = '__all__'


class PhoneNumberSerializer(serializers.ModelSerializer):
    airport = AirportSerializer()

    class Meta:
        model  = models.PhoneNumber
        fields = '__all__'