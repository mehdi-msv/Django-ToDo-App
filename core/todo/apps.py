from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"

    def ready(self):
        """
        This method is called when the Django application is ready.
        It sets up periodic tasks using the scheduler module.
        """
        from .scheduler import setup_periodic_tasks

        setup_periodic_tasks()  # Initialize periodic tasks
