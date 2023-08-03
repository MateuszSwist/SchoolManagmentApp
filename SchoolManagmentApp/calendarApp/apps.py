from django.apps import AppConfig


class CalendarappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calendarApp'

    def ready(self):
        import calendarApp.signals