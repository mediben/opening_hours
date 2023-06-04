""" app file """
import os
import json

from flask import request, abort, jsonify
from werkzeug.exceptions import HTTPException

from opening_hours import create_app
from opening_hours.serializer import WorkingHours
from opening_hours.service import format_to_humain_time

app = create_app()


@app.errorhandler(Exception)
def handle_error(error):
    code = 400
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify(error_message=str(error)), code


@app.route("/", methods=["GET", "POST"])
def display_hours():
    if request.method == "GET":
        return "Update this with how to use the API"
    if request.method == "POST":
        data = request.data

        working_hours = WorkingHours(data)

        response_data = format_to_humain_time(working_hours.data)

        response = app.response_class(
            response=json.dumps(response_data), mimetype="application/json"
        )
        return response


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5230, debug=True)
