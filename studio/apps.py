from django.apps import AppConfig


class StudioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studio'
    label = 'studio'

    def ready(self):
        import studio.signals 
