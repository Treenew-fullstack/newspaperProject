from .celery import app as celery_app


# Настройка для асинхронного взаимодействия Celery
__all__ = ('celery_app',)
