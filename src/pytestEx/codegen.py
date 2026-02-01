# playwright codegen generated file

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/")
    page.get_by_role("link", name="MX Player").click()
    page.get_by_role("link", name="New & Hot").click()
    page.get_by_role("link", name="Web Series").click()
    page.get_by_role("link", name="Movies", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)