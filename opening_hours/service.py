""" service layer """

from .utils.constant import EVENT_TYPE_OPEN
from .utils.formatter import format_unix_time, format_output


def format_to_humain_time(data: dict) -> str:
    """
    Convert input unix times to human readable times
    """
    converted_times = convert_input_times(data)
    human_times = format_output(converted_times)
    return human_times


def convert_input_times(data: dict) -> str:
    """
    Parses serialized input data and convert it to human times
    """
    opening_time = None
    opening_day = None
    custom_closing_time = None
    humain_readeable_opening_hours = {}

    for day, day_status in data.items():
        humain_readeable_opening_hours[day] = []
        for status in day_status:
            if status["type"] == EVENT_TYPE_OPEN:
                opening_time = format_unix_time(status["value"])
                opening_day = day
            else:
                closing_time = format_unix_time(status["value"])
                if opening_time is not None:
                    humain_readeable_opening_hours[opening_day].append(
                        f"{opening_time} - {closing_time}"
                    )
                else:
                    custom_closing_time = closing_time

    if custom_closing_time:
        humain_readeable_opening_hours[day].append(
            f"{opening_time} - {custom_closing_time}"
        )
    return humain_readeable_opening_hours
