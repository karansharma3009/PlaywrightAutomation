from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page loaded:", page.url)

def on_request(request):
    print("Request made:", request.url)



with sync_playwright() as playwright:   
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.on("load", on_load) # event listener for page load
    page.on("request", on_request) # event listener for network requests
    page.on("close", lambda: print("Page closed")) # event listener for page close
    page.on("download", lambda download: print("Download started:", download.url)) # event listener for downloads
    page.goto("https://bootswatch.com/default/")
    page.locator("a.nav-link.dropdown-toggle").first.click()
    link = page.locator("div a.dropdown-item[href='../brite/']")
    link.click(force=True)
    print(page.title())
    browser.close()
