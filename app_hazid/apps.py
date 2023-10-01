from django.apps import AppConfig


class AppHazidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_hazid'

    def ready(self):
        import app_hazid.signals