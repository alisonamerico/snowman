# import pytest
# from django.urls import reverse
# from pytest_django.fixtures import django_user_model
# from rest_framework import status
# # from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient

# # from touristspots.base.models import User


# @pytest.fixture
# def create_user(db):
#     email = 'foo@email.com'
#     password = 'bar'
#     user = django_user_model.objects.create_user(email=email, password=password)
#     return user


# @pytest.fixture
# def api_client(create_user):
#     # token, _ = Token.objects.get(user=create_user)
#     client = APIClient()
#     client.credentials(HTTP_AUTHORIZATION='JWT ' + token.key)
#     return client


# def test_api_root_view_sucess(api_client):
#     resp = api_client.get(reverse('api/v1/'))
#     assert resp.status_code == status.HTTP_200_OK


# # @pytest.fixture
# # def api_client_unauthorized(create_user):
# #     token = Token.objects.get(user=create_user)
# #     client = APIClient()
# #     client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
# #     return client


# # def test_api_root_view_unauthorized(api_client_unauthorized):
# #     resp = api_client_unauthorized.get('api/v1/')
# #     assert resp.status_code == status.HTTP_401_UNAUTHORIZED
