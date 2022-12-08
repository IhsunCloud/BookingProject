from .base import INSTALLED_APPS

# Custom Project
INSTALLED_APPS.append('booking')
INSTALLED_APPS.append('cart')
INSTALLED_APPS.append('user')

# 3rd-Party Packages
INSTALLED_APPS.append('django_otp',)
INSTALLED_APPS.append('djoser')
INSTALLED_APPS.append('django_otp.plugins.otp_totp')
INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')

# DRF Stuff
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}