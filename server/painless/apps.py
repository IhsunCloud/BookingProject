from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PainlessConfig(AppConfig):
    name = 'painless'
    verbose_name = _('Painless')
    verbose_name_plural = _('Painless')