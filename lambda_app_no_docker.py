from datetime import datetime


def lambda_handler(event, context):
    try:
        time_string = event["time_string"]
        datetime_now = datetime.now()
        hour = int(time_string[0])
        time_string_datetime = datetime_now.replace(hour=hour,
                                                    minute=0,
                                                    second=0).strftime(
                                                    "%m-%d-%Y, %H:%M:%S %p")
        return {
            'statusCode': 200,
            'body': time_string_datetime
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': "needs time_string as request body"
        }
