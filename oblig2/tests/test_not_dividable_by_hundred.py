import oblig2

def test_not_dividable_by_100():
    bool_notdivide100 = True if oblig2.year % 100 > 0 else False
    assert bool_notdivide100 == oblig2.isLeapYear(oblig2.year)