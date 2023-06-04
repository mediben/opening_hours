""" serializer file test """
import json
import pytest

from ..serializer import WorkingHours

pytest_plugins = ["docker_compose"]

def test_above_range_integer():
    """ unit test """
    invalid_input = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 3600074847},
            {"type": "close", "value": 13000},
        ],
    }
    input_data = json.dumps(invalid_input)

    with pytest.raises(Exception) as error:
        WorkingHours(input_data)

    assert 'Timestamp not correct for "tuesday"' in str(error.value)


def test_below_range_integer():
    """ unit test """
    invalid_input = {
        "monday": [],
        "tuesday": [{"type": "open", "value": -1}, {"type": "close", "value": 13000}],
    }

    input_data = json.dumps(invalid_input)
    with pytest.raises(Exception) as error:
        WorkingHours(input_data)

    assert 'Timestamp not correct for "tuesday"' in str(error.value)


def test_invalid_type():
    """ unit test """
    invalid_input = {
        "monday": [],
        "tuesday": [
            {"type": "on-holidays", "value": 36000},
            {"type": "close", "value": 64800},
        ],
    }

    input_data = json.dumps(invalid_input)
    with pytest.raises(Exception) as error:
        WorkingHours(input_data)

    assert 'Wrong type input for "tuesday"' in str(error.value)


def test_invalid_duplicate_type():
    """ unit test """
    invalid_input = {
        "monday": [],
        "tuesday": [{"type": "open", "value": 36000}, {"type": "open", "value": 64800}],
    }

    input_data = json.dumps(invalid_input)
    with pytest.raises(Exception) as error:
        WorkingHours(input_data)

    assert 'Wrong duplicate type found for "tuesday"' in str(error.value)


def test_wrong_week_type():
    """ unit test """
    invalid_input = {
        "monday": [{"type": "close", "value": 36000}],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800},
        ],
    }

    input_data = json.dumps(invalid_input)
    with pytest.raises(Exception) as error:
        WorkingHours(input_data)

    assert "Need to have different type from start type" in str(error.value)


def test_success():
    """ unit test """
    valid_input = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800},
        ],
    }
    input_data = json.dumps(valid_input)

    expected_output = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 36000},
            {"type": "close", "value": 64800},
        ],
    }

    serialized_data = WorkingHours(input_data)

    assert expected_output, serialized_data.data
