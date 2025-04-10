from django.urls import reverse
import pytest
from rest_framework.response import Response

# Create your tests here.


@pytest.fixture
def valid_data():
    """
    Fixture providing valid data for task creation.

    Returns:
        dict: A dictionary containing valid task data.
    """
    # Define and return a dictionary with valid task data
    return {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False,
    }


@pytest.fixture
def create_task(admin_client, valid_data) -> Response:
    """
    Fixture to create a task via the API, returns the response.
    """
    url = reverse("todo:api-v1:task-list")
    # Post the valid data to the API
    response = admin_client.post(url, valid_data, content_type="application/json")
    return response


@pytest.mark.django_db
class TestModel:
    def test_create_task_response_201(self, create_task):
        """
        Test that creating a task returns a 201 response status code.
        """
        # The response status code should be 201
        assert create_task.status_code == 201

    def test_update_task_with_patch_response_200(
        self, valid_data, admin_client, create_task
    ):
        """
        Test that updating a task with patch method returns a 200 response status code
        and the task is updated correctly.
        """
        # Retrieve the latest task created
        task_id = create_task.data["id"]

        # Prepare URL and data for updating the task
        update_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        updated_data = valid_data.copy()
        updated_data["title"] = "Updated Task"

        # Send a PATCH request to update the task
        response = admin_client.patch(
            update_url, updated_data, content_type="application/json"
        )
        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the task's title is updated
        assert response.data["title"] == "Updated Task"

    def test_update_task_with_put_response_200(
        self, valid_data, admin_client, create_task
    ):
        """
        Test that updating a task with put method returns a 200 response status code
        and the task is updated correctly.
        """
        # Retrieve the latest task created
        task_id = create_task.data["id"]

        # Prepare URL and data for updating the task
        update_url = reverse("todo:api-v1:task-detail", kwargs={"pk": task_id})
        updated_data = valid_data.copy()
        updated_data["title"] = "Updated Task"

        # Send a PUT request to update the task
        response = admin_client.put(
            update_url, updated_data, content_type="application/json"
        )
        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the task's title is updated
        assert response.data["title"] == "Updated Task"
