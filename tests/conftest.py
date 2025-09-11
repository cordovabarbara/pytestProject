import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


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


#Fixture para inicializar el navegador
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

#Makes the fixtures available to all test files in the same directory.
#scope="class" in conftest.py
#The fixture is executed only once per class, not for each function.
#Setup runs at the beginning of the class.
#Teardown (after the yield) runs at the end of the class.