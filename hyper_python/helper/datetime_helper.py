"""
This module provides utility functions for parsing and comparing dates.

Functions:
- parse_dates(dates: [str], format: str = DATE_FORMAT) -> [datetime]:
    Parses a list of date strings into datetime objects.
- get_earlist_date(dates: [datetime]) -> datetime:
    Returns the most recent datetime from a list of datetime objects.
- find_index_of_most_recent_date_str(dates: [str], format: str = DATE_FORMAT) -> int:
    Finds the index of the most recent date string in the list.

Usage example:
    dates = ["2023-10-04", "2023-10-03", "2023-10-05"]
    format = "%Y-%m-%d"
    parsed_dates = parse_dates(dates, format)
    most_recent_date = get_earlist_date(parsed_dates)
    index_of_most_recent = find_index_of_most_recent_date_str(dates, format)
"""

from datetime import datetime
from hyper_python import DATE_FORMAT


def parse_dates(dates: [str], date_format: str = DATE_FORMAT) -> [datetime]:
    """
    :param dates: A list of date strings to be parsed.
    :param date_format: Date format string that conforms to strftime directives.
    :return: A list of datetime objects parsed from the input strings.
    """
    return [datetime.strptime(date, date_format) for date in dates]


def get_earlist_date(dates: [datetime]) -> datetime:
    """
    :param dates: A list of datetime objects.
    :return: The most recent datetime from the list.
    """
    return max(dates)

def find_index_of_most_recent_date_str(dates: [str], date_format: str = DATE_FORMAT) -> int:
    """
    :param dates: List of date strings to be evaluated.
    :param date_format: Format in which the dates are specified.
    :return: Index of the most recent date in the list.
    """
    dates_parsed = parse_dates(dates, date_format)
    return dates_parsed.index(get_earlist_date(dates_parsed))
