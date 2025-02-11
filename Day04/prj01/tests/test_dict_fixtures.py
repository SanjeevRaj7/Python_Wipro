import pytest


@pytest.fixture
def sample_data():
    return {"Key": "value"}

def test_sample_data(sample_data):
    assert sample_data["Key"] == "value"