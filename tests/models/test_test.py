import pytest


@pytest.mark.tttest
def test_true(db_inspector):
    print("\n-------> ASSERT True == True\n")
    assert True

