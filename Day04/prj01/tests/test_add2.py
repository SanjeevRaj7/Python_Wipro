import pytest

def test_01():
    assert 1+1 == 2
@pytest.mark.skip("Known Bug") # it will skip the testcase02
def test_02():
    assert 2*3 == 6