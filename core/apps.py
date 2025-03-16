# core/apps.py
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.signals  # Импорт сигналов при запуске приложения
