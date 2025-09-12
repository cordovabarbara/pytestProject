
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.login import LoginPage
from pageObjects.shop import ShopPage



def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    #Login
    shop_page = LoginPage(driver).login()

    #Add product to cart
    shop_page.add_product_to_cart("Samsung Note 8")

    #Go to cart
    shop_page.go_to_cart()

