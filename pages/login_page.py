import re
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def goto(self, base_url: str):
        self.page.goto(base_url)

    def login(self, user: str, pw: str):
        self.username.fill(user)
        self.password.fill(pw)
        self.login_btn.click()
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))