import pytest

##run with pytest test_isLeapYear.py -s
year = int(2020)

def isLeapYear(year: int):
    if year % 4 == 0 and year % 100 > 0:
        leapYear_cond1 = True
        print(str(year) + " is a leap year!")
        return leapYear_cond1
    elif year % 400 == 0:
        leapYear_cond2 = True
        print(str(year) + " is a leap year!")
        return leapYear_cond2
    elif year % 4 > 0:
        leapYear_cond3 = False
        print(str(year) + " is not a leap year!")
        return leapYear_cond3
    elif year % 100 == 0 and year % 400 > 0:
        leapYear_cond4 = False
        print(str(year) + " is not a leap year!")
        return leapYear_cond4
    else:
        print(str(year) + " is a leap year!")
        return False

isLeapYear(year)

##To run non-leap year tests: pytest test_isLeapYear.py -s -m notleapyear -v
##To run leap year tests: pytest test_isLeapYear.py -s -m leapyear -v

##acceptance tests for determining non-leap years
@pytest.mark.notleapyear  
def test_dividable_by_100():
    assert year % 100 == 0

@pytest.mark.notleapyear
def test_not_dividable_by_4():
    assert year % 4 > 0

@pytest.mark.notleapyear
def test_not_dividable_by_400():
    assert year % 400 > 0
    
##Acceptance tests for leap years
@pytest.mark.leapyear
def test_not_dividable_by_100():
    assert year % 100 > 0

@pytest.mark.leapyear
def test_dividable_by_4():
    assert year % 4 == 0

@pytest.mark.leapyear
def test_dividable_by_400():
    assert year % 400 == 0