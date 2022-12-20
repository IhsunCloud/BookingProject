import math
import random


def generate_otp(password_len=6):
	"""
	Reusable function to generate an OTP password.
	"""
	passwd_len = password_len
	DIGITS = '0123456789'
	OTP	= ''

	for number in range(passwd_len):
		OTP += DIGITS[math.floor(random.random() * 10)]
	return OTP