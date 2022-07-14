import arrow


def datetime_to_milliseconds(datetime: arrow.Arrow):
    return datetime.timestamp() * 1000
