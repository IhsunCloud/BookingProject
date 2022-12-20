# import pyjion
from .base import INSTALLED_APPS


# Custom Project
INSTALLED_APPS.append('agency')
INSTALLED_APPS.append('api')
INSTALLED_APPS.append('booking')
INSTALLED_APPS.append('cart')
INSTALLED_APPS.append('hotel')
INSTALLED_APPS.append('painless')
INSTALLED_APPS.append('user')

# 3rd-Party Packages
INSTALLED_APPS.append('django_otp')
INSTALLED_APPS.append('django_otp.plugins.otp_totp')
INSTALLED_APPS.append('djoser')
INSTALLED_APPS.append('model_utils')
INSTALLED_APPS.append('phonenumbers')
# INSTALLED_APPS.append('pyjion')
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')

CART_SESSION_ID = 'cart'

# pyjion.set_optimization_level(0)