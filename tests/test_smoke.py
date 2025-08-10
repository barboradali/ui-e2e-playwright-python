from playwright.sync_api import expect
from utils.config import BASE_URL

def test_homepage_loads(page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Swag Labs")
