import pytest

##run with pytest test_isLeapYear.py -s
year = int(input("Enter a year: "))

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

isLeapYear()

##To run non-leap year tests: pytest test_isLeapYear.py -s -m notleapyear -v
##To run leap year tests: pytest test_isLeapYear.py -s -m leapyear -v

##acceptance tests for determining non-leap years
@pytest.mark.notleapyear  
def test_dividable_by_100():
    bool_divide100 = True if year % 100 == 0 else False
    assert bool_divide100 == isLeapYear(year)

@pytest.mark.notleapyear
def test_not_dividable_by_4():
    bool_notdivide4 = True if year % 4 > 0 else False
    assert bool_notdivide4 == isLeapYear(year)

@pytest.mark.notleapyear
def test_not_dividable_by_400():
    bool_notdivide400 = True if year % 400 > 0 else False
    assert bool_notdivide400 == isLeapYear(year)
    
##Acceptance tests for leap years
@pytest.mark.leapyear
def test_not_dividable_by_100():
    bool_notdivide100 = True if year % 100 > 0 else False
    assert bool_notdivide100 == isLeapYear(year)

@pytest.mark.leapyear
def test_dividable_by_4():
    bool_divide4 = True if year % 4 == 0 else False
    assert bool_divide4 == isLeapYear(year)

@pytest.mark.leapyear
def test_dividable_by_400():
    bool_divide400 = True if year % 400 == 0 else False
    assert bool_divide400 == isLeapYear(year)