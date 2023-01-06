from rest_framework import serializers
from hotel import models


class AdultSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Adult
        fields = '__all__'


class UnderageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Underage
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Hotel
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Image
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Passenger
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Phone
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Reviews
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.Room
        fields = '__all__'