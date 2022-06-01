from datetime import datetime
import json


def lambda_handler(event, context):
    try:
        try:
            time_string = event["time_string"]
        except KeyError:
            response = json.loads(event["body"])
            time_string = response["time_string"]
        datetime_now = datetime.now()
        hour = datetime.strptime(time_string, '%I%p').hour
        time_string_datetime = datetime_now.replace(hour=hour,
                                                    minute=0,
                                                    second=0).strftime(
                                                    "%m-%d-%Y, %H:%M:%S %p")
        return json.dumps({"response": time_string_datetime})
    except KeyError:
        return json.dumps({"response": "needs time_string as request body"})
