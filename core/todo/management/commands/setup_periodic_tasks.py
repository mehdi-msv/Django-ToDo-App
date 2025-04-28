from django.core.management.base import BaseCommand
from todo.scheduler import setup_periodic_tasks

class Command(BaseCommand):
    help = "Setup periodic tasks"

    def handle(self, *args, **options):
        """
        Creates or updates a periodic task that runs every 10 minutes
        and deletes all completed tasks.
        """
        setup_periodic_tasks()
        self.stdout.write(self.style.SUCCESS('Periodic tasks set up successfully.'))
