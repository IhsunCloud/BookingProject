from rest_framework import serializers
from home import models

from ..user.serializers import UserSerializer


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Home
        fields = '__all__'


class AdultSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Adult
        fields = '__all__'


class UnderageSerializer(serializers.ModelSerializer):
    class Meta:
        model =  models.Underage
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    adult = AdultSerializer(many=True)
    underage = UnderageSerializer(many=True)
    home  = HomeSerializer(many=True)

    class Meta:
        model =  models.Passenger
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=True)

    class Meta:
        model =  models.Bookmark
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=True)

    class Meta:
        model =  models.Image
        fields = '__all__'



class PhoneSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=True)

    class Meta:
        model =  models.Phone
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=True)

    class Meta:
        model =  models.Reviews
        fields = '__all__'







