from datetime import datetime

import pytest
from src.hyper_python.helper.datetime_helper import parse_dates


# test cases for the parse_dates function

def test_parse_dates():
    dates = ["2024-02-29", "2022-12-31", "2022-01-01"]
    expected_output = [
        datetime.strptime("2024-02-29", "%Y-%m-%d"),
        datetime.strptime("2022-12-31", "%Y-%m-%d"),
        datetime.strptime("2022-01-01", "%Y-%m-%d"),
    ]
    assert parse_dates(dates) == expected_output


def test_parse_dates_with_custom_format():
    dates = ["29-02-2024", "31-12-2022", "01-01-2022"]
    expected_output = [
        datetime.strptime("29-02-2024", "%d-%m-%Y"),
        datetime.strptime("31-12-2022", "%d-%m-%Y"),
        datetime.strptime("01-01-2022", "%d-%m-%Y"),
    ]
    assert parse_dates(dates, "%d-%m-%Y") == expected_output


def test_parse_dates_with_invalid_dates():
    dates = ["2024-02-30", "2022-13-31", "2022-01-32"]
    with pytest.raises(ValueError):
        parse_dates(dates)


def test_parse_dates_with_invalid_format():
    dates = ["2024-02-29", "2022-12-31", "2022-01-01"]
    with pytest.raises(ValueError):
        parse_dates(dates, "%Y-%d-%m")
