# 13021326

import pytest

from my_file import most_frequent

def test_most_frequent1():
    L = [1, 1, 1, 6, 6, 6]
    assert most_frequent(L) == 1

def test_most_frequent2():
    L = [1, 5, -3, 2, -7]
    assert most_frequent(L) == -7

def test_most_frequent3():
    L = [3.0, -4.2, 9, 2, 3]
    assert most_frequent(L) == 3

def test_most_frequent4():
    L = [2, 2.0, 2, 2.0]
    assert most_frequent(L) == 2

def test_most_frequent5():
    L = [-2, -2, -2, -2]
    assert most_frequent(L) == -2