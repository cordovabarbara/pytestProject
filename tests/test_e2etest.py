import json
import pytest

test_data_path = r"C:\Users\Anais\PycharmProjects\pytestProject\data\test_e2etest.json"
with open (test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(login, test_list_item):
    #Login
    shop_page = login(
        test_list_item["userEmail"],
        test_list_item["userPassword"]
    )

    #Add product to cart
    shop_page.add_product_to_cart(test_list_item["productName"])

    #Go to cart
    checkout_confirmation = shop_page.go_to_cart()

    #Checkout
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address(test_list_item["deliveryAddress"])
    checkout_confirmation.validate_order()
