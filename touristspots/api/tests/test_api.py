import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.fixture
def create_user(db):
    email = 'foo@email.com'
    password = 'bar'
    user = get_user_model().objects.create_user(email=email, password=password)
    return user


@pytest.fixture
def api_client(create_user):
    token = Token.objects.create(user=create_user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


def test_user_create(db):
    get_user_model().objects.create_user('foo@email.com', 'bar')
    assert get_user_model().objects.count() == 1


def test_api_root_view_sucess_request(api_client):
    resp = api_client.get(reverse('api:api-root'))
    assert resp.status_code == status.HTTP_200_OK


def test_api_root_content_view(api_client):
    resp = api_client.get(reverse('api:api-root'))
    assert resp.status_code == status.HTTP_200_OK


def test_touristspots_view_authorized_request(api_client):
    resp = api_client.get('/api/v1/touristspots/')
    assert resp.status_code == status.HTTP_200_OK


def test_favorites_view_authorized_request(api_client):
    resp = api_client.get('/api/v1/favorites/')
    assert resp.status_code == status.HTTP_200_OK


@pytest.fixture
def api_client_unauthorized():
    client = APIClient()
    return client


def test_touristspots_view_unauthorized_request(api_client_unauthorized):
    resp = api_client_unauthorized.get('/api/v1/touristspots/')
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_favorite_view_unauthorized_request(api_client_unauthorized):
    resp = api_client_unauthorized.get('/api/v1/favorites/')
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED


def test_create_touristpot(api_client):
    resp = api_client.post(
        '/api/v1/touristspots/',
        data={
            "name": "Walmart Avenida Recife",
            "geographical_location": {
                "type": "Point",
                "coordinates": [
                    -3888297.88354,
                    -904454.87184
                ]
            },
            "category": "PARK"
        },
        format='json'
    )
    assert resp.status_code == status.HTTP_201_CREATED


# def test_update_touristpot(api_client):
#     resp = api_client.put(
#         'touristspot-detail/1/',
#         data={
#             {
#                 "id": 1,
#                 "picture": "http://0.0.0.0:8000/media/pic_folder/none/no-img.jpg",
#                 "name": "Parque Santos Dumont",
#                 "geographical_location": {
#                     "type": "Point",
#                     "coordinates": [
#                         -34.9040816111268,
#                         -8.141266676521594
#                     ]
#                 },
#                 "category": "PARK",
#                 "created": "2020-07-28T03:00:05.794300Z",
#                 "modified": "2020-07-28T03:29:59.351760Z"
#             }
#         },
#         format='json'
#     )
#     assert resp.status_code == status.HTTP_200_OK


# def test_delete_touristpot(api_client):
#     resp = api_client.delete(
#         '/api/v1/touristspots/1/',
#         data={
#             "id": 1,
#             "picture": "http://0.0.0.0:8000/media/pic_folder/none/no-img.jpg",
#             "name": "Parque Santos Dumont",
#             "geographical_location": {
#                 "type": "Point",
#                 "coordinates": [
#                     -34.9040816111268,
#                     -8.141266676521594
#                 ]
#             },
#             "category": "PARK",
#             "created": "2020-07-28T03:00:05.794300Z",
#             "modified": "2020-07-28T03:29:59.351760Z"
#         },
#         format='json'
#     )
#     assert resp.status_code == status.HTTP_204_NO_CONTENT
