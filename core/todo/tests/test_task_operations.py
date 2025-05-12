from django.urls import reverse
import pytest


from ..models import Task


@pytest.mark.django_db
class TestTaskOperations:
    def test_create_task_adds_to_db(self, create_task, valid_data):
        """
        Test that creating a task via the API adds the task to the database.

        Ensures that a task is correctly created using the provided valid data
        and that the task's title matches the expected value.
        """
        create_task
        assert Task.objects.count() == 1
        task = Task.objects.first()
        assert task.title == valid_data["title"]

    def test_anonymous_user_cannot_create_task(self, api_client, valid_data):
        """
        Tests that an anonymous user cannot create a task via the API.

        """
        url = reverse("todo:api-v1:task-list")
        api_client.post(url, data=valid_data)
        assert Task.objects.count() == 0
        assert Task.objects.last() is None

    @pytest.mark.parametrize("method", ["put", "patch"])
    def test_update_task(self, user_client, create_task, valid_data, method):
        """
        Tests that the PATCH and PUT endpoints update a task.

        Verifies that the endpoints update the task with the provided data.
        """
        task_id = create_task.data["id"]
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})

        updated_data = valid_data.copy()
        updated_data["title"] = f"Updated Title with {method.upper()}"
        updated_data["complete"] = True

        getattr(user_client, method)(url, data=updated_data)
        task = Task.objects.get(id=task_id)
        assert task.title == f"Updated Title with {method.upper()}"
        assert task.complete is True

    @pytest.mark.parametrize("method", ["put", "patch"])
    def test_anonymous_user_cannot_update_task(
        self, api_client, create_task, valid_data, method
    ):
        """
        Tests that an anonymous user cannot update a task via the API.

        Verifies that anonymous users cannot update tasks and ensures.
        """
        task_id = create_task.data["id"]
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})

        updated_data = valid_data.copy()
        updated_data["title"] = f"Updated Title with {method.upper()}"
        updated_data["complete"] = True

        api_client.logout()

        getattr(api_client, method)(url, data=updated_data)
        task = Task.objects.get(id=task_id)
        assert task.title == create_task.data["title"]
        assert task.complete is False

    def test_delete_task(self, user_client, create_task):
        """
        Tests that a task can be successfully deleted via the API.

        Ensures that the DELETE endpoint removes the specified task from the
        database.
        """
        task_id = create_task.data["id"]
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})

        user_client.delete(url)
        assert not Task.objects.filter(id=task_id).exists()

    def test_anonymous_user_cannot_delete_task(self, api_client, create_task):
        """
        Tests that an anonymous user cannot delete a task via the API.

        Verifies that an anonymous user cannot delete tasks as expected.
        """
        # Get the task ID from the created task fixture
        task_id = create_task.data["id"]
        # Construct the URL for the task detail endpoint
        url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})

        # Log out the current user to simulate an anonymous user
        api_client.logout()

        # Attempt to delete the task as an anonymous user
        api_client.delete(url)

        # Verify that the task still exists in the database
        task = Task.objects.get(id=task_id)
        assert task is not None
