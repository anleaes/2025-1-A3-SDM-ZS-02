from django.apps import AppConfig


class AnimalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.animal'
    verbose_name = 'Animal'