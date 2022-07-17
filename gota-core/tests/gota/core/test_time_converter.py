import arrow

from src.gota.core.time_converter import datetime_to_milliseconds


def test_datetime_to_milliseconds():
    # using a fixed epoch here to test it without implementing the same logic from the method under
    # test here
    expected_milliseconds = 1657842544174
    datetime = arrow.get(expected_milliseconds)
    assert datetime_to_milliseconds(datetime) == expected_milliseconds
