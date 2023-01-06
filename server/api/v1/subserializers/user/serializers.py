import random
import pyotp
from rest_framework import serializers
from painless.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'phone_number')


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = (
	  		'phone_number',
		)

	def create(self, validated_data):

		instance = self.Meta.model(**validated_data)

		global totp
		totp = pyotp.TOTP('base32secret3232')
		totp.now() # e.g.: `492039`
		secret = pyotp.random_base32()
		totp   = pyotp.TOTP(secret, interval=300)
		otp    = totp.now()

		instance = self.Meta.model.objects.update_or_create(
	  		**validated_data,
			defaults = dict(
				otp  = str(random.randint(1000 , 9999)
			)))[0]

		instance.save()
		return instance


class VerifyOTPSerializer(serializers.ModelSerializer):
		class Meta:
			model  = User
			fields = ['phone_number','otp']

		def create(self,validated_data):
			instance = self.Meta.model(**validated_data)

			keywords = "123456789"
			result   = "@" + str(''.join(
	   			random.choices(keywords, k=6)
		  	))

			instance = self.Meta.model.objects.update_or_create(
	   			**validated_data,
		  		defaults = dict(
					username = result,
				 	name = instance.phone_number,
				))[0]

			instance.save()
			return instance