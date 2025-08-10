from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.add_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart_link = page.locator(".shopping_cart_link")

    def assert_loaded(self):
        expect(self.title).to_have_text("Products")

    def add_item_and_open_cart(self):
        self.add_backpack.click()
        self.cart_link.click()