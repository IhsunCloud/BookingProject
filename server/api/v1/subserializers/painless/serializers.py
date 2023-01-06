from rest_framework import serializers

from painless.utils.models.address_model import AddressModel


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = '__all__'