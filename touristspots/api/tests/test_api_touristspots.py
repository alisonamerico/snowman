from touristspots.conftest import APIClient, pytest
from touristspots.api.models import TouristSpot
from rest_framework import status


def test_touristspots_view_authorized_request(api_client):
    resp = api_client.get('/api/v1/touristspots/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.fixture
def api_client_unauthorized():
    client = APIClient()
    return client


def test_touristspots_view_unauthorized_request(api_client_unauthorized):
    resp = api_client_unauthorized.get('/api/v1/touristspots/')
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_touristpot(api_client):
    resp = api_client.post(
        '/api/v1/touristspots/',
        data={
            "name": "Museu do Teste",
            "geographical_location": {
                "type": "Point",
                "coordinates": [
                    -34.88358735552661,
                    -8.067472892722346
                ]
            },
            "category": "MUSEUM"
        },
        format='json'
    )
    assert resp.status_code == status.HTTP_201_CREATED


@pytest.fixture
def touristpot():
    api_touristspot = TouristSpot.objects.create()
    return api_touristspot


@pytest.fixture
def update_touristpot(api_client, touristpot):
    resp = api_client.put(
        f'/api/v1/touristspots/{touristpot.id}/',
        data={
            "id": 1,
            "name": "Museu do Teste2",
            "geographical_location": {
                "type": "Point",
                "coordinates": [
                    -34.88358735552661,
                    -8.067472892722346
                ]
            },
            "category": "MUSEUM",
            "created": "2020-08-06T23:57:56.733523Z",
            "modified": "2020-08-07T01:19:37.381841Z"
        },
        format='json',)
    return resp


def test_update_touristpot(update_touristpot, touristpot):
    # assert update_touristpot.data["name"] == touristpot.name
    assert update_touristpot.status_code == status.HTTP_200_OK


@pytest.fixture
def delete_touristpot(api_client, touristpot):
    resp = api_client.delete(
        f'/api/v1/touristspots/{touristpot.id}/',
        data={
            "id": 1,
            "name": "Museu do Teste2",
            "geographical_location": {
                "type": "Point",
                "coordinates": [
                    -34.88358735552661,
                    -8.067472892722346
                ]
            },
            "category": "MUSEUM",
            "created": "2020-08-06T23:57:56.733523Z",
            "modified": "2020-08-07T01:19:37.381841Z"
        },
        format='json',)
    return resp


def test_delete_touristpot(delete_touristpot):
    assert delete_touristpot.status_code == status.HTTP_204_NO_CONTENT
