import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

#Makes the fixtures available to all test files in the same directory.