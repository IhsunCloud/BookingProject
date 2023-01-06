from django.utils.translation import gettext_lazy as _

from .base import INSTALLED_APPS


# Custom Project
INSTALLED_APPS.append('agency')
INSTALLED_APPS.append('airplane')
INSTALLED_APPS.append('airport')
INSTALLED_APPS.append('api')
INSTALLED_APPS.append('booking')
INSTALLED_APPS.append('bus')
INSTALLED_APPS.append('checkout')
INSTALLED_APPS.append('hotel')
INSTALLED_APPS.append('home')
INSTALLED_APPS.append('painless')
INSTALLED_APPS.append('tour')
# 3rd-Party Packages
INSTALLED_APPS.append('django_extensions')
INSTALLED_APPS.append('django_otp')
INSTALLED_APPS.append('django_otp.plugins.otp_totp')
INSTALLED_APPS.append('djoser')
INSTALLED_APPS.append('holidays')
INSTALLED_APPS.append('model_utils')
INSTALLED_APPS.append('phonenumbers')
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')

CART_SESSION_ID = 'checkout'

# PhoneNumberField Stuff
PHONENUMBER_DEFAULT_FORMAT = "E164"
PHONENUMBER_DEFAULT_REGION = "CA"
