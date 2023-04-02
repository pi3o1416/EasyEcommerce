from django.apps import AppConfig


class BannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'banner'

    def ready(self):
        try:
            from . import signals as _
        except Exception:
            pass
