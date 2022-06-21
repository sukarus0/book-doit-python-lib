import calendar

def test_leap_year():
    assert calendar.isleap(0) == True
    assert calendar.isleap(2000) == True
    assert calendar.isleap(2100) == False
