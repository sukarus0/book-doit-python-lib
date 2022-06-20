"""
    005 test
"""
import datetime as dt
import pytest


@pytest.fixture
def date_list():
    """
    Define first day and test day
    """
    first_day = dt.date(2001, 5, 24)
    test_day = dt.date(2022, 6, 20)

    date_list = {"first_day": first_day, "test_day": test_day}

    return date_list


def test_day_100(date_list):
    """
    Check 100-day anniversary
    """
    delta = dt.timedelta(days=100)
    day_100 = date_list["first_day"] + delta

    assert day_100 == dt.date(2001, 9, 1)


def test_day_count_after_firstday(date_list):
    """
    How many days from first day
    """
    delta = date_list["test_day"] - date_list["first_day"]

    assert delta == dt.timedelta(days=7697)


def test_day_of_week_first_day(date_list):
    """
    Check day of week on first day
    """
    day_of_week = dt.datetime.weekday(date_list["first_day"])

    assert day_of_week == 3
