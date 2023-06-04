""" service test file """
import pytest

from ..service import format_to_humain_time
from ..service import convert_input_times

pytest_plugins = ["docker_compose"]

# Default payload data
data = {
    "monday": [],
    "tuesday": [{"type": "open", "value": 36000}, {"type": "close", "value": 64800}],
    "wednesday": [],
    "thursday": [{"type": "open", "value": 36000}, {"type": "close", "value": 64800}],
    "friday": [{"type": "open", "value": 36000}],
    "saturday": [{"type": "close", "value": 3600}, {"type": "open", "value": 36000}],
    "sunday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 43200},
        {"type": "close", "value": 75600},
    ],
}


@pytest.mark.parametrize(
    "day, times",
    [
        ("monday", []),
        ("tuesday", ["10 AM - 6 PM"]),
        ("wednesday", []),
        ("thursday", ["10 AM - 6 PM"]),
        ("friday", ["10 AM - 1 AM"]),
        ("saturday", ["10 AM - 1 AM"]),
        ("sunday", ["12 PM - 9 PM"]),
    ],
)

def test_convert_input_times(day, times):
    """Test for the service's parsing function"""
    parsed_times_dict = convert_input_times(data)
    assert parsed_times_dict[day] == times


def test_format_to_humain_time():
    """Test the main service end to end"""
    expected_output = (
        "The restaurant on Monday: Closed Tuesday: 10 AM - 6 PM "
        "Wednesday: Closed Thursday: 10 AM - 6 PM Friday: 10 AM - 1 AM "
        "Saturday: 10 AM - 1 AM Sunday: 12 PM - 9 PM"
    )
    assert format_to_humain_time(data) == expected_output


def test_overflowing_closing_time():
    """Test when a restaurant does not close the same day"""
    new_data = data.copy()
    new_data["monday"] = [{"type": "close", "value": 95400}]
    new_data["sunday"].append({"type": "open", "value": 81000})
    parsed_times_dict = convert_input_times(new_data)
    assert parsed_times_dict["sunday"] == ["12 PM - 9 PM", "10:30 PM - 2:30 AM"]
