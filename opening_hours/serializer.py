""" serializer layer """
import json

from .utils.constant import EVENT_TYPE_CLOSE, EVENT_TYPE_OPEN


class WorkingHours:
    """ WorkingHours class"""

    def __init__(self, data: dict) -> dict:
        print("debug for data!", type(data))

        self.data = json.loads(data)
        self.validate_times()

    def validate_times(self):
        """
        Valide times input data to be correct
        """
        previous_status_type = None
        first_status_type = None
        timestap_range = range(0, 86400)

        for day, statuses in self.data.items():
            for status in statuses:
                if status["value"] not in timestap_range:
                    raise Exception(f'Timestamp not correct for "{day}".')

                if status["type"] not in [EVENT_TYPE_OPEN, EVENT_TYPE_CLOSE]:
                    raise Exception(f'Wrong type input for "{day}".')

                if status["type"] == previous_status_type:
                    raise Exception(f'Wrong duplicate type found for "{day}".')
                else:
                    previous_status_type = status["type"]

                if first_status_type is None:
                    first_status_type = status["type"]

        if first_status_type == previous_status_type:
            raise Exception("Need to have different type from start type.")

        return self.data
