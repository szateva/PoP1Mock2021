import pytest

from question6 import *

def test_day_of_year1():
    assert day_of_year(3, 1) == 2  # must be True
def test_day_of_year2():
    assert day_of_year(10, 5) == 130  # must be True
def test_day_of_year2():
    assert day_of_year(31, 6) == -1  # must be True