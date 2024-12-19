import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from main import fetch_data, filter_users_by_geolocation, calculate_completion_percentage
from unittest.mock import patch

# Mock data
mock_users = [
    {"id": 1, "name": "User1", "address": {"geo": {"lat": "-35", "lng": "50"}}},
    {"id": 2, "name": "User2", "address": {"geo": {"lat": "10", "lng": "80"}}},
]
mock_todos = [
    {"userId": 1, "completed": True},
    {"userId": 1, "completed": False},
    {"userId": 2, "completed": True},
    {"userId": 2, "completed": True},
]

LAT_RANGE = (-40, 5)
LON_RANGE = (5, 100)


# Test fetch_data
@patch("main.requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.json.return_value = mock_users
    mock_get.return_value.status_code = 200
    result = fetch_data("http://example.com")
    assert result == mock_users
    mock_get.assert_called_once_with("http://example.com")


# Test filter_users_by_geolocation
def test_filter_users_by_geolocation():
    filtered_users = filter_users_by_geolocation(mock_users, LAT_RANGE, LON_RANGE)
    assert len(filtered_users) == 1
    assert filtered_users[0]["name"] == "User1"


# Test calculate_completion_percentage
def test_calculate_completion_percentage():
    percentage = calculate_completion_percentage(mock_todos, 1)
    assert percentage == 50.0

    percentage = calculate_completion_percentage(mock_todos, 2)
    assert percentage == 100.0

    percentage = calculate_completion_percentage(mock_todos, 3)  # No todos
    assert percentage == 0.0
