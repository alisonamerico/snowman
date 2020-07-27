
import pytest
from django.urls import reverse
from rest_framework import status

from touristspots.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == status.HTTP_200_OK


def test_title(resp):
    assert_contains(resp, '<title>Touristspots - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Home</a>')


def test_home_menu_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Home</a>')


def test_api_root_link(resp):
    assert_contains(resp, f'href="{reverse("api:api-root")}">Api</a>')
