from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    """
    Fixture to provide a Rest Framework API client.

    Returns:
        APIClient: An instance of APIClient for testing API requests.
    """
    return APIClient()


@pytest.fixture
def user_client(api_client):
    """
    Fixture providing an authenticated API client.

    This fixture creates a test user and authenticates the provided API client
    with the test user, allowing for testing of protected endpoints.

    Args:
        api_client (APIClient): The API client fixture to be authenticated.

    Returns:
        APIClient: An authenticated API client.
    """
    # Get the user model
    User = get_user_model()

    # Create a test user
    test_user = User.objects.create_user(
        username="testuser", password="testpassword123"
    )

    # Authenticate the API client with the test user
    api_client.force_authenticate(user=test_user)

    # Return the authenticated API client
    return api_client


@pytest.fixture
def valid_data():
    """
    Fixture providing valid data for task creation.

    Returns:
        dict: A dictionary containing valid task data.
    """
    return {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False,
    }


@pytest.fixture
def create_task(user_client, valid_data) -> Response:
    """
    Fixture to create a task via the API, returns the response.
    """
    url = reverse("todo:api-v1:task-list")
    # Post the valid data to the API for task creation
    response = user_client.post(url, valid_data)
    return response
