from celery import shared_task
from .models import Task


@shared_task
def delete_completed_tasks():
    """
    A periodic task that deletes all completed tasks from the database.
    """
    Task.objects.filter(complete=True).delete()
