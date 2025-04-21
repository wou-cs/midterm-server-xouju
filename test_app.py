import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_returns_success(client):
    response = client.get('/api/calcs/1')
    assert response.status_code == 200


def test_returns_json(client):
    response = client.get('/api/calcs/1')
    assert response.content_type == 'application/json'


def test_one_incremented_is_two(client):
    response = client.get('/api/calcs/1')
    calcs = response.get_json()
    assert calcs["dec"] == 0


def test_one_modulo_twelve_is_one(client):
    response = client.get('/api/calcs/1')
    calcs = response.get_json()
    assert calcs["hex"].upper() == "0X1"


def test_fifteen_hex_is_f(client):
    response = client.get('/api/calcs/15')
    validity = response.get_json()
    calcs = response.get_json()
    assert calcs["hex"].upper() == "0XF"


def test_remaining_special_cases_are_decremented(client):
    for i in (5, 7, 11, 13, 17, 23):
        response = client.get(f"/api/calcs/{i}")
        calcs = response.get_json()
        assert calcs["dec"] == i - 1


def test_non_integer_results_in_error(client):
    response = client.get('/api/calcs/foobar')
    assert response.status_code == 400