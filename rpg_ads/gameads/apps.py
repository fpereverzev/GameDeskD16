from django.apps import AppConfig


class GameadsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gameads'

    def ready(self):
        import gameads.signals
