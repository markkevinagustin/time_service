from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["POST"])
def time_service():
    try:
        requests = request.json
        time_string = requests["time_string"]
        datetime_now = datetime.now()
        hour = int(time_string[0])
        time_string_datetime = datetime_now.replace(hour=hour,
                                                    minute=0).strftime(
                                                    "%m-%d-%Y, %H:%M:%S %p")
        return jsonify(time_string_datetime)
    except KeyError:
        return jsonify("needs time_string as request body")
