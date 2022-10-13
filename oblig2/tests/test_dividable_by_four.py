import pytest
import oblig2

def test_dividable_by_4():
    bool_divide4 = True if oblig2.year % 4 == 0 else False
    assert bool_divide4 == oblig2.isLeapYear(oblig2.year)