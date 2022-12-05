from django.db import models
from django.utils.translation import gettext_lazy as _


class STATUS(models.TextChoices):
    DRAFT     = 'D', _('Draft'),
    PUBLISHED = 'P', _('Published'),
