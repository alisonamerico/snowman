from touristspots.urls import urlpatterns


def test_urls_len():
    """
    Checks the amount of urls in the api
    """
    assert 9 == len(urlpatterns)
