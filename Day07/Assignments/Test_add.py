#8
#Write a parametrized test case using Pytest to validate multiple inputs and expected outputs for a function.


import pytest

def add(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(-1,-2,-3),])

def test_add(a,b,expected):
    assert add(a,b) == expected




