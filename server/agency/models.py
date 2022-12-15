from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import SluggedModel, TimeStampedModel

class Agency(SluggedModel, TimeStampedModel):
    pass