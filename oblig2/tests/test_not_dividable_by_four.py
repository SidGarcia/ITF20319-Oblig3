import oblig2, pytest

def test_not_dividable_by_4():
    bool_notdivide4 = True if oblig2.year % 4 > 0 else False
    assert bool_notdivide4 == oblig2.isLeapYear(oblig2.year)