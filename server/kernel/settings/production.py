from decouple import config

from .base import *
from .packages import *
from .secure import *


DEBUG = config('DEBUG', default=False, cast=bool)
