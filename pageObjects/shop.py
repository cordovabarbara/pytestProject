from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.checkout_confirmation import CheckoutConfirmation


class ShopPage:
    shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
    products_cards = (By.XPATH, "//div[@class='card h-100']")
    cart_button = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")   # up - right

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_shop(self):
        self.driver.find_element(*self.shop_link).click()

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(*self.products_cards)

        for product in products:
            name = product.find_element(By.XPATH, ".//h4/a").text
            if name.strip().lower() == product_name.strip().lower():
                product.find_element(By.XPATH, ".//button").click()
                print(f"✅ Product added to cart: {product_name}")
                break
        else:
            raise Exception(f"❌ Product '{product_name}' no found.")

        # wait until cart update
        self.wait.until(
            EC.text_to_be_present_in_element(self.cart_button, "Checkout ( 1 )")
        )

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
        return CheckoutConfirmation(self.driver)
