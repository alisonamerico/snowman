from touristspots.urls import urlpatterns


def test_urls_len():
    assert 8 == len(urlpatterns)
