import pytest
import oblig2

def test_dividable_by_4():
    assert oblig2.isLeapYear() % 4 == 0