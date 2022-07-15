import arrow


def datetime_to_milliseconds(datetime: arrow.Arrow):
    return int(datetime.timestamp() * 1000)
