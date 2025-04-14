from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from ...models import Task


class Command(BaseCommand):
    help = "Create a task with 'task 5' title for a random user"

    def __init__(self):
        """
        Initializes the command with a Faker instance for generating
        random user data.
        """
        super().__init__()
        self.faker = Faker()

    def handle(self, *args, **options):
        """
        Handles the command execution.

        This function creates a new user with random data and then creates a new task for this user.
        The task is created with a fixed title "task 5" and assigns the newly created user as its author.
        A success message is written to the standard output displaying the task's id and the user's full name.
        """
        # Create a new user with random data
        user = get_user_model().objects.create_user(
            username=self.faker.user_name(),
            email=self.faker.email(),
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            password="@M/12345",
        )

        # Create a new task with the title 'task 5' and the newly created user as the author
        task = Task.objects.create(
            title="task 5", author=user, complete=random.choice([True, False])
        )

        # Write a success message to the standard output
        self.stdout.write(
            self.style.SUCCESS(
                f"Task with id:{task.id} created for {user.first_name} {user.last_name}"
            )
        )
