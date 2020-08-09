
from touristspots.conftest import get_user_model
from django.urls import reverse
from rest_framework import status


def test_user_create(db):
    get_user_model().objects.create_user('foo@email.com', 'bar')
    assert get_user_model().objects.count() == 1


def test_api_root_view_sucess_request(api_client):
    resp = api_client.get(reverse('api:api-root'))
    assert resp.status_code == status.HTTP_200_OK


def test_api_root_content_view(api_client):
    resp = api_client.get(reverse('api:api-root'))
    assert resp.status_code == status.HTTP_200_OK
