from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
    products_cards = (By.XPATH, "//div[@class='card h-100']")
    cart_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")   # arriba a la derecha

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_shop(self):
        self.driver.find_element(*self.shop_link).click()

    def add_product_to_cart(self, product_name):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.products_cards)
        )

        for product in products:
            productName = product.find_element(By.XPATH, ".//h4/a").text.strip()
            if productName.lower() == product_name.lower():
                add_button = product.find_element(By.CSS_SELECTOR, "div.card-footer button.btn.btn-info")
                add_button.click()
                break


        cart_text = self.wait.until(
            EC.presence_of_element_located(self.cart_button)
        ).text
        print("Cart button text:", cart_text)

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()


