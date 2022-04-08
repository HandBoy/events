import uuid

from apps.events.models import Application
from rest_framework.test import APITestCase


def generata_application():
    return Application.objects.create(
        name="app_01",
        uuid=uuid.uuid4()
    )


class PostEventsAPITestCase(APITestCase):
    def setUp(self):
        self.url = "/api/v1/events/"
        self.headers = {
            "HTTP_APPLICATION": generata_application().uuid,
        }

    def test_post_event_without_application(self):
        # Give
        data = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        # When
        response = self.client.post(self.url, json=data)

        # Then
        self.assertEqual(response.status_code, 400)
    
    def test_post_event_application_does_not_exists(self):
        # Give
        data = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        # When
        response = self.client.post(self.url, json=data)

        # Then
        self.assertEqual(response.status_code, 400)    
    
    def test_post_event_without_requirements_fields(self):
        # Give
        data = {}
        # When
        response = self.client.post(self.url, json=data)

        # Then
        self.assertEqual(response.status_code, 400)

    def test_post_event_with_invalid_timestamp(self):
        # Give
        data = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/"
            },
            "timestamp": "01/01/2021 09:15:27.243860"
        }
        # When
        response = self.client.post(
            self.url, data=data, format="json", **self.headers
        )
        # Then
        self.assertEqual(response.status_code, 400)

    def test_post_event(self):
        # Give
        data = {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/"
            },
            "timestamp": "2021-01-01 09:15:27.243860"
        }
        # When
        response = self.client.post(
            self.url, data=data, format="json", **self.headers
        )
        # Then
        self.assertEqual(response.status_code, 201)

