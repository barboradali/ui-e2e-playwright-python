cat << 'EOF' > README.md
# UI E2E Automation Framework (Python + Playwright + Pytest)

## Overview
This project is a UI end-to-end automation test suite for the [Sauce Demo](https://www.saucedemo.com) application. It is built using Python, Playwright, and Pytest, following the Page Object Model design pattern. The framework is integrated with Allure for advanced reporting and is ready for continuous integration using GitHub Actions.

## Features
- End-to-end checkout flow automation
- Page Object Model (POM) for maintainable test code
- Cross-browser testing (Chromium, Firefox, WebKit)
- Parallel execution using pytest-xdist
- Allure HTML reporting
- Configurable via environment variables
- CI/CD-ready with GitHub Actions

## Project Structure
.
├── pages/                  # Page Object classes for each UI page
├── tests/                  # Test cases
├── utils/                  # Config and helper functions
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
├── Dockerfile              # Containerized test environment
├── docker-compose.yml      # Services for tests and Allure reporting
├── .github/workflows/      # CI configuration for GitHub Actions
└── README.md               # Project documentation

## Installation, Running Tests, and Generating Reports
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ui-e2e-playwright-python.git
cd ui-e2e-playwright-python

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .\.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
python -m playwright install

# Environment variables (optional overrides)
export BASE_URL="https://www.saucedemo.com"
export HEADLESS="1"  # "0" for headed
export DEMO_USER="standard_user"
export DEMO_PASS="secret_sauce"

# Run all tests in headless mode
pytest -q

# Run in headed mode
pytest --headed -q

# Run tests in parallel
pytest -n auto -q

# Run tests and generate Allure results
pytest --alluredir=allure-results -q

# Serve Allure report locally
allure serve allure-results

Author: Barbora Dali
barboradali@gmail.com
GitHub: https://github.com/barboradali
EOF
