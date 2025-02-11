#13
#Write a Pytest test case that parameterizes a function with multiple inputs and expected outputs.

import pytest
def prime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

@pytest.mark.parametrize("n,expected",[(2,True),(4,False),(5,True),(1,False)])

def test_prime(n, expected):
    assert prime(n) == expected