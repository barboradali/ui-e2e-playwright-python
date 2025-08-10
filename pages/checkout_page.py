from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first = page.locator("#first-name")
        self.last = page.locator("#last-name")
        self.zip = page.locator("#postal-code")
        self.cont = page.locator("#continue")
        self.finish = page.locator("#finish")
        self.complete_header = page.locator(".complete-header")

    def fill_shipping(self, first, last, postal):
        self.first.fill(first)
        self.last.fill(last)
        self.zip.fill(postal)
        self.cont.click()

    def finish_order_and_assert(self):
        self.finish.click()
        expect(self.complete_header).to_have_text("Thank you for your order!")
