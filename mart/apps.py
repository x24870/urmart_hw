from django.apps import AppConfig


class MartConfig(AppConfig):
    name = 'mart'

    def ready(self):
        import mart.signals