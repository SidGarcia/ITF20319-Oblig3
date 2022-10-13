from oblig2 import isLeapYear, year

def test_not_dividable_by_4():
    assert isLeapYear(year) == False
    ##== (year % 4 > 0)