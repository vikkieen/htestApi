import pytest
@pytest.fixture(scope='class',autouse=True)
def session_fixture1():
    print("停车")
    yield
    print("出发")