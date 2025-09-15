from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutConfirmation:
    checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")
    country_input = (By.ID, "country")
    country_option = (By.LINK_TEXT, "Spain")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "[type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()


    def enter_delivery_address(self,countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success" in successText