from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json


def setup_periodic_tasks():
    """
    Creates or updates a periodic task that runs every 10 minutes
    and deletes all completed tasks.
    """
    # Define schedule properties
    every = 10  # Task runs every 10 minutes
    period = IntervalSchedule.MINUTES

    # Find or create the interval schedule
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=every,
        period=period,
    )

    # Define task properties
    task_name = "Delete completed tasks periodically"
    task_path = "todo.tasks.delete_completed_tasks"
    task_kwargs = json.dumps({})  # No additional arguments needed

    # Find the task if it exists, or create it if it doesn't
    periodic_task, created = PeriodicTask.objects.get_or_create(
        name=task_name,
        defaults={
            "interval": schedule,
            "task": task_path,
            "kwargs": task_kwargs,
        },
    )

    # If the task already exists, check if any details need updating
    if not created:
        updated = False

        # Update interval if it has changed
        if periodic_task.interval != schedule:
            periodic_task.interval = schedule
            updated = True

        # Update task path if it has changed
        if periodic_task.task != task_path:
            periodic_task.task = task_path
            updated = True

        # Update task kwargs if they have changed
        if periodic_task.kwargs != task_kwargs:
            periodic_task.kwargs = task_kwargs
            updated = True

        # Save the task if any updates were made
        if updated:
            periodic_task.save()
