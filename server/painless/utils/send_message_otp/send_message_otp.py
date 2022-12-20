from django.conf import settings

from kavenegar import KavenegarAPI

from .generate_otp import generate_otp


def send_message_otp(phone_number, message=None):
	"""
	Reusable function to sending SMS, using Kavenegar API.

	ihsun@tuta.io
	"""
	api = KavenegarAPI(settings.SMS_API_KEY)	# Import Your API_KEY.
	sms_sender = settings.SMS_SENDER			# Import Your Sender. (PhoneNumber)

	msg = message if message is not None else generate_otp()

	params = {
		'sender'  : sms_sender,
		'receptor': phone_number,
		'message' : msg
	}
	response = api.sms_send(params)

	print(response.text)