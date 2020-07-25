from django.test import Client


def test_status_code(client: Client):
    """Test status code home"""
    resp = client.get('/')
    assert resp.status_code == 200
