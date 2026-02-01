import pytest
from playwright.sync_api import sync_playwright



# this fixture supplies a Playwright page object for browser interactions
@pytest.fixture(scope="session")
def page_1():
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        return browser.new_page()

def test_example(page_1):
    page_1.goto("https://www.amazon.in")
    title = page_1.title()
    assert title == "Example Domain"