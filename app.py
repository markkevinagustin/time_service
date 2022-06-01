from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)


@app.route("/", methods=["POST"])
def time_service():
    try:
        requests = request.json
        time_string = requests["time_string"]
        datetime_now = datetime.now()
        hour = int(time_string[0])
        time_string_datetime = datetime_now.replace(hour=hour,
                                                    minute=0,
                                                    second=0).strftime(
                                                    "%m-%d-%Y, %H:%M:%S %p")
        return jsonify(time_string_datetime)
    except KeyError:
        return jsonify("needs time_string as request body")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
