""" formatter file """
import arrow


def format_unix_time(timestamp: int) -> str:
    """
    Converts Unix timestamp to a human readable UTC 12 hours AM/PM
    """
    current_time = arrow.Arrow.fromtimestamp(timestamp).to("UTC")
    formatted_time = current_time.format("h:mm:ss A")
    if current_time.format("ss") == "00":
        formatted_time = current_time.format("h:mm A")
        if current_time.format("mm") == "00":
            formatted_time = current_time.format("h A")

    return formatted_time


def format_output(data: dict) -> str:
    """
    Refine restaurant formated opening hours
    """
    restaurant_times = ["The restaurant on"]
    for day, times in data.items():
        if times:
            restaurant_times.append(f'{day.title()}: {", ".join(times)}')
        else:
            restaurant_times.append(f"{day.title()}: Closed")

    restaurant_times_text = " ".join([str(line) for line in restaurant_times])

    return restaurant_times_text


# def format_time(timestamp: int) -> str:
#     """
#     Converts Unix timestamp to a human readable time UTC 12 hours
#     """
#     converted_time = datetime.utcfromtimestamp(timestamp)
#     formatted_time = converted_time.strftime('%I:%M:%S %p')
#     # if converted_time.format('%S') == '00':
#     #     formatted_time = converted_time.strftime('%I:%M %p')
#     #     if converted_time.format('%M') == '00':
#     #         formatted_time = converted_time.strftime('%I: %p')

#     return formatted_time
