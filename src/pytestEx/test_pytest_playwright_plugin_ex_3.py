import pytest
from playwright.sync_api import sync_playwright,Page

# we used playwright-pytest plugin to create a fixture for Playwright page object here. 

@pytest.fixture
def page(page: Page):
    page.goto("https://www.amazon.in")
    page.get_by_text("MX Player").click()
    yield page
    page.close()
    print("Browser Closed Successfully")



def test_example(page: Page):
    title = page.title()
    print("-----"+title)
    assert title == "Amazon miniTV - Watch Free Web Series, Movies, Short Films & K-Dramas Online"
