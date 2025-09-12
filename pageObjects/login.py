from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    username_input = (By.ID, "username")
    password_input = (By.NAME, "password")
    sign_button = (By.ID, "signInBtn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def set_username(self, username):
        element = self.wait.until(EC.visibility_of_element_located(self.username_input))
        element.clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input))
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.sign_button).click()

    def login(self,username="rahulshettyacademy", password="learning"):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
