from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DFCoreConfig(AppConfig):
    name = "df_core"
    verbose_name = _("DjangoFlow Core")

    def ready(self):
        ...
