from rest_framework import serializers

from painless.utils.models.address_model import Address
from painless.utils.models.address_model import AddressModel


class AddressModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    address = AddressModelSerializer(many=True)

    class Meta:
        model = Address
        fields = '__all__'