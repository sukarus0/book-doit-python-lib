"""
    006
"""
import datetime as dt
import pytest


@pytest.fixture
def firstDay():
    return dt.date(2001, 5, 24)


def test_100_day(firstDay):
    result = firstDay + dt.timedelta(days=100)

    assert result == dt.date(2001, 9, 1)

