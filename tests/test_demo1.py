#Any pytest file should start with test_
#pytest method names should start with test
# skip test with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello World")

@pytest.mark.xfail
def test_greting():
    print("Good Morning")