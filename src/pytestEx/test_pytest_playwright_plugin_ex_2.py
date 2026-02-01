import pytest
from playwright.sync_api import sync_playwright,Page

# we used playwright-pytest plugin to create a fixture for Playwright page object here. 

def test_example(page: Page):
    page.goto("https://www.example.com")
    title = page.title()
    print("-----"+title)
    assert title == "Example Domain"
