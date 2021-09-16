from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicar.schedule'
    verbose_name = "agenda"

    def ready(self):
        from . import signals  # noqa
