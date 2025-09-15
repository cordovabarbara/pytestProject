import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pageObjects.login import LoginPage


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
    return ["Barbara", "Cordova", "barbara@gmail.com"]


@pytest.fixture(params=[("barbara", "cordova"), "chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param

from pageObjects.login import LoginPage

@pytest.fixture
def login(browserInstance):
    def _login(userEmail, userPassword):
        driver = browserInstance
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        return LoginPage(driver).login(userEmail, userPassword)
    return _login



# Fixture para inicializar el navegador
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = Options()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-features=PasswordManager,AutofillSaveCard")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--log-level=3")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(5)


    yield driver
    driver.quit()
