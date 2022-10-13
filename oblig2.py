import pytest

year = int(2000)

def isLeapYear(n: int):
    if year % 4 == 0 and year % 100 > 0:
        print(str(year) + " is a leap year!")
        return True
    elif year % 400 == 0:
        print(str(year) + " is a leap year!")
        return True
    elif year % 4 > 0:
        print(str(year) + " is not a leap year!")
        return False
    elif year % 100 == 0 and year % 400 > 0:
        print(str(year) + " is not a leap year!")
        return False
    else:
        print(str(year) + " is a leap year!")
        return False