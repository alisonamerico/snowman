# import pytest
# from django.urls import reverse
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient

# from touristspots.base.models import User


# @pytest.fixture
# def create_user(db):
#     email = 'foo@email.com'
#     password = 'bar'
#     user = User.objects.create_user(email=email, password=password)
#     return user


# @pytest.fixture
# def token(create_user):
#     token, _ = Token.objects.create(user=create_user)
#     return token


# @pytest.fixture
# def api_client(create_user, token):
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
#     return client


# def test_get_environments(api_client):
#     resp = api_client.get('/api/v1/')
#     assert resp.status_code == 200
