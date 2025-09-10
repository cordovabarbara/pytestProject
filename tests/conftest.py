import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Barbara", "Cordova", "barbara@gmail.com"]

@pytest.fixture(params=[("barbara", "cordova"),"chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param


#Makes the fixtures available to all test files in the same directory.
#scope="class" in conftest.py
#The fixture is executed only once per class, not for each function.
#Setup runs at the beginning of the class.
#Teardown (after the yield) runs at the end of the class.