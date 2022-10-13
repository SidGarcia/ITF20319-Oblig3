import oblig2

def test_not_dividable_by_100():
    assert oblig2.isLeapYear() % 100 > 0