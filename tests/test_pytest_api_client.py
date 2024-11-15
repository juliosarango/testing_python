import pytest
from unittest.mock import Mock
import requests

from src.api_client import get_location


@pytest.fixture
def mock_data():
    yield {
        "countryName": "USA",
        "regionName": "Florida",
        "cityName": "MIAMI",
        "countryCode": "US",
    }


def test_get_location_return_expected_data(mocker, mock_data):

    mocker.patch("src.api_client.requests.get").return_value.json.return_value = (
        mock_data
    )

    result = get_location("8.8.8.8")

    assert result.get("country") == "USA"
    assert result.get("region") == "Florida"
    assert result.get("city") == "MIAMI"
    assert result.get("code") == "US"


# create a test with side_effect
def test_get_location_return_side_effect(mocker, mock_data):
    mocker.patch("src.api_client.requests.get").side_effect = [
        requests.exceptions.RequestException("Service Unavailable"),
        Mock(status_code=200, json=lambda: mock_data),
    ]

    with pytest.raises(requests.exceptions.RequestException):
        get_location("8.8.8.8")

    result = get_location("8.8.8.8")
    assert result.get("country") == "USA"
    assert result.get("region") == "Florida"
    assert result.get("city") == "MIAMI"
    assert result.get("code") == "US"


def test_get_location_return_side_effect_with_invalid_ip(mocker):
    mocker.patch("src.api_client.requests.get").side_effect = [
        ValueError("8.8.0 does not appear to be an IPv4 or IPv6 address"),
        Mock(status_code=200, json=lambda: mock_data),
    ]

    with pytest.raises(ValueError):
        get_location("8.8.0")
