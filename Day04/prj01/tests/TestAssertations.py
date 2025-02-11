def test_assert():
    assert 1 + 2 == 3, "Addition got failed" # it will pass when the value is failed


#EXCEPTIONS
import pytest
def test_exception():
    with pytest.raises(ZeroDivisionError): # or we can use Exception instead of zero and for any error
        1/0
