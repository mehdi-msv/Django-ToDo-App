from django.urls import reverse
import pytest


# Create your tests here.

@pytest.mark.django_db
class TestEndpoints:
    @pytest.mark.parametrize(
        "method, url_name, expected_status",
        [
            ("get", "todo:api-v1:task-list", 200),
            ("get", "todo:api-v1:task-detail", 200),
            ("post", "todo:api-v1:task-list", 201),
            ("put", "todo:api-v1:task-detail", 200),
            ("patch", "todo:api-v1:task-detail", 200),
            ("delete", "todo:api-v1:task-detail", 204),
        ],
    )
    def test_authenticated_user_status_codes(
        self, method, url_name, expected_status, user_client, create_task, valid_data
    ):
        """
        Test that the API endpoints return the expected status code.
        """
        if "detail" in url_name:
            task_id = create_task.data["id"]
            url = reverse(url_name, kwargs={"pk": task_id})
        else:
            url = reverse(url_name)
                    
        if method in ["post", "put", "patch"]:
            response = getattr(user_client, method)(url, data=valid_data)
        else:
            response = getattr(user_client, method)(url)
                    
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "method, url_name",
        [
            ("get", "todo:api-v1:task-list"),
            ("get", "todo:api-v1:task-detail"),
            ("post", "todo:api-v1:task-list"),
            ("put", "todo:api-v1:task-detail"),
            ("patch", "todo:api-v1:task-detail"),
            ("delete", "todo:api-v1:task-detail"),
        ],
    )
    def test_task_anonymous_response_401(
        self, method, url_name, api_client, create_task, valid_data
    ):
        """
        Test that the API endpoints return a 401 response status code as an anonymous user.
        """
        if "detail" in url_name:
            task_id = create_task.data["id"]
            url = reverse(url_name, kwargs={"pk": task_id})
        else:
            url = reverse(url_name)
                    
        api_client.logout()
                
        if method in ["post", "put", "patch"]:
            response = getattr(api_client, method)(url, data=valid_data)
        else:
            response = getattr(api_client, method)(url)
                    
        assert response.status_code == 401
