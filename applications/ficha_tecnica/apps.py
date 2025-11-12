from django.apps import AppConfig


class FichaTecnicaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.ficha_tecnica'

    def ready(self):
        import applications.ficha_tecnica.signals