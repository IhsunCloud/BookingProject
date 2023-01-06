from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers import (
	RegisterSerializer,
	VerifyOTPSerializer
)

from painless.models import User
from painless.model_utils import send_message_otp


class RegisterViewSet(ModelViewSet):
	serializer_class  = RegisterSerializer
	http_method_names = ['get', 'post',]
	queryset = User.objects.all()

	def post(self, request):
		phone_number = request.data['phone_number']
		data = User.objects.filter(phone_number = phone_number).first()

		if data is not None:
			serializer = self.serializer_class(data = request.data)
			phone_number = request.data['phone_number']
			if serializer.is_valid(raise_exception = True):
				instance = serializer.save()
				content  = {
					'phone_number': instance.phone_number,
					'otp': instance.otp
				}
				phone_number = instance.phone_number
				otp = instance.otp
				print("Success")
				send_message_otp(phone_number, otp)
				return Response(content, status = status.HTTP_201_CREATED)
			error = {"Error": "Login in Failed"}
			return Response(error, status = status.HTTP_400_BAD_REQUEST)
		else:
			serializer   = self.serializer_class(data = request.data)
			phone_number = request.data['phone_number']

		if serializer.is_valid(raise_exception = True):
			instance = serializer.save()
			content  = {
				'phone_number': instance.phone_number,
				'otp': instance.otp
			}
			phone_number = instance.phone_number
			otp = instance.otp
			send_message_otp(phone_number, otp)
			return Response(content, status = status.HTTP_201_CREATED)
		else:
			error = {'Error': 'Sign Up Failed'}
			return Response(error, status = status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(ModelViewSet):
	serializer_class  = VerifyOTPSerializer
	http_method_names = ['get', 'post',]

	def post(self, request):
		serializer = VerifyOTPSerializer(data = request.data)
		phone_number = request.data['phone_number']
		otp_sent   = request.data['otp']

		if phone_number and otp_sent:
			old_data = User.objects.filter(phone_number = phone_number)
			if old_data is not None:
				old_data = otp_sent.first()
				otp = old_data.otp
				if str(otp) == str(otp_sent):
					serializer   = self.serializer_class(data = request.data)
					phone_number = request.data['phone_number']
					if serializer.is_valid(raise_exception = True):
						instance = serializer.save()
						content  = {
							'phone_number': instance.phone_number,
							'otp': instance.otp,
						}
						return Response(content, status = status.HTTP_201_CREATED)
				else:
					res = {'status': False, 'detail': 'OTP incorrect, please try again'}
					return Response(res)