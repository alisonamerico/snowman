from touristspots.conftest import APIClient, pytest
from rest_framework import status


def test_pictures_view_authorized_request(api_client):
    resp = api_client.get('/api/v1/pictures/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.fixture
def api_client_unauthorized():
    client = APIClient()
    return client


def test_pictures_view_unauthorized_request(api_client_unauthorized):
    resp = api_client_unauthorized.get('/api/v1/pictures/')
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
