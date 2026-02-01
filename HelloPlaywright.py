from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=5000)
    page = browser.new_page()
    page.goto("https://www.makemytrip.com")
    page.locator('[data-cy="closeModal"]').click()
    print(page.title())
    holiday_icon = page.get_by_text(text="Holiday Packages",exact=True)
    holiday_icon.nth(0).click()
    page.get_by_test_id("fromCity").highlight()
    from_city = page.get_by_test_id("fromCity")
    from_city.click()
    enter_city = page.get_by_placeholder("Enter City")
    enter_city.clear()
    enter_city.fill("Bangalore")
    #from_city.clear().fill("Bangalore")
    browser.close()