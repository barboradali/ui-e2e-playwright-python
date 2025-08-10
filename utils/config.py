
import os
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
HEADLESS = os.getenv("HEADLESS", "1") == "1"
USER = os.getenv("DEMO_USER", "standard_user")
PASS = os.getenv("DEMO_PASS", "secret_sauce")
