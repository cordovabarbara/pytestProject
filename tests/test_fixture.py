import pytest

@pytest.fixture()
def setup():
    print("I will executing first")
    yield
    print("I will executing last")

def test_fixtureDemo(setup):
    print("I will execute  steps in fixtureDemo method")
