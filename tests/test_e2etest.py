
from pageObjects.login import LoginPage



def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    #Login
    shop_page = LoginPage(driver).login()

    #Add product to cart
    shop_page.add_product_to_cart("iphone X")

    #Go to cart
    checkout_confirmation = shop_page.go_to_cart()

    #Checkout
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("spain")
    checkout_confirmation.validate_order()

