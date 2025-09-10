#Any pytest file should start with test_
#pytest method names should start with test
# skip test with @pytest.mark.skip
#fixtures are used as setup  and ter down methods for test cases conftest file to generalize
#fixture and make it available to all test cases
import pytest


@pytest.mark.smoke

def test_firstProgram(setup):
    print("Hello World")

@pytest.mark.xfail
def test_greting():
    print("Good Morning")

