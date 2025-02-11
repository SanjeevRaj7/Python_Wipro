import pytest
@pytest.mark.parametrize("input,expected",[(2,4),(3,9)])

def test_parameters(input,expected):
    assert input**2 == expected
    #assert input**2!=expected
