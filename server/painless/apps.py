from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PainlessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'painless'
    app_label = 'painless'
    verbose_name = _('iPainless')
    verbose_name_plural = _('iPainless')
