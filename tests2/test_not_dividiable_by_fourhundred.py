import oblig2

def test_not_dividable_by_400():
    assert oblig2.isLeapYear() % 400 > 0