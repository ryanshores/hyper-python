from datetime import datetime
from .. import DATE_FORMAT


def parse_dates(dates: [str], format: str = DATE_FORMAT) -> [datetime]:
    """
    :param dates: A list of date strings to be parsed.
    :param format: Date format string that conforms to strftime directives.
    :return: A list of datetime objects parsed from the input strings.
    """
    return [datetime.strptime(date, format) for date in dates]


def get_earlist_date(dates: [datetime]) -> datetime:
    """
    :param dates: A list of datetime objects.
    :return: The most recent datetime from the list.
    """
    return max(dates)

def find_index_of_most_recent_date_str(dates: [str], format: str = DATE_FORMAT) -> int:
    dates_parsed = parse_dates(dates, format)
    return dates_parsed.index(get_earlist_date(dates_parsed))