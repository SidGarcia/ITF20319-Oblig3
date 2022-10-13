import oblig2

def test_not_dividable_by_400():
    bool_notdivide400 = True if oblig2.year % 400 > 0 else False
    assert bool_notdivide400 == oblig2.isLeapYear(oblig2.year)