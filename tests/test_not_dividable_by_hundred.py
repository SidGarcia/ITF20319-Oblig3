from oblig2 import isLeapYear, year

def test_not_dividable_by_100():
    ##assert not oblig2.isLeapYear() % 100 > 0
    assert isLeapYear(year) == False