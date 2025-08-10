import re
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.locator("#checkout")

    def checkout(self):
        expect(self.page).to_have_url(re.compile(r".*/cart\.html"))
        self.checkout_btn.click()