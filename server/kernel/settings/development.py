import imp
from decouple import config

from .base import *
from .packages import *
from .secure import *


ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False