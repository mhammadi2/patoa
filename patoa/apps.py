from django.apps import AppConfig


class PatoaConfig(AppConfig):
    name = 'patoa'

    def ready(self):
        import patoa.signals