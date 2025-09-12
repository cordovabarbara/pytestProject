from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.products_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def open_shop(self):
        self.driver.find_element(*self.shop_link).click()

    def add_product_to_cart(self, product_name):
        products = self.wait.until(EC.presence_of_all_elements_located(self.products_cards))

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()
                break


    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()