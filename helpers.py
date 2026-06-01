from datetime import datetime

def datetime_to_str(time: datetime):
    return time.strftime("%Y-%m-%dT%H:%M:%S")