from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True ,args=["--disable-http2"])
    page = browser.new_page()
    context = browser.new_context(
    user_agent=(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
)
    page.goto("https://www.makemytrip.com")
    page.locator('[data-cy="closeModal"]').click()
    page.locator("//p[@data-cy='LoginHeaderText']").click()
    page.locator("img.signInByEmailButton").click()
    page.get_by_placeholder("Enter Email Address").type("holidays-qa@makemytrip.com",delay=100)
    page.get_by_role("button",name="Continue").click()
    page.get_by_role("input",name="password").type("Holidays0987",delay=100)
    page.get_by_role("button",name="Login").highlight()
    page.pause()   
    browser.close() 
