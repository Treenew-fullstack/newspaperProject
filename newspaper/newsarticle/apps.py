from django.apps import AppConfig


class NewsarticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsarticle'

# Импортирование сигналов
    def ready(self):
        from . import signals
