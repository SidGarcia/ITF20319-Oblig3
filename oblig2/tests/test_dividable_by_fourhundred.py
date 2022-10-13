import oblig2

def test_dividable_by_400():
    bool_divide400 = True if oblig2.year % 400 == 0 else False
    assert bool_divide400 == oblig2.isLeapYear(oblig2.year)