from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL, USER, PASS

def test_full_checkout(page):
    login = LoginPage(page)
    inv = InventoryPage(page)
    cart = CartPage(page)
    chk = CheckoutPage(page)

    login.goto(BASE_URL)
    login.login(USER, PASS)
    inv.assert_loaded()
    inv.add_item_and_open_cart()
    cart.checkout()
    chk.fill_shipping("Ada", "Lovelace", "42424")
    chk.finish_order_and_assert()