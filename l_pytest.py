import pytest
import leapyear

def test1():
    result = leapyear.is_leap(2000)
    assert result == True

def test2():
    result = leapyear.is_leap(2100)
    assert result == False

def test3():
    result = leapyear.is_leap(1998)
    assert result == False