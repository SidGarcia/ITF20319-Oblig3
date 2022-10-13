from oblig2 import isLeapYear, year

def test_not_dividable_by_400():
    ##assert not oblig2.isLeapYear() % 400 > 0
    assert isLeapYear(year) == False