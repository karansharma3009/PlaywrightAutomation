from playwright.sync_api import Page
from .locators import HOME
class HomePage:

    def __init__(self, page: Page):
         self.page = page
         page.goto("https://www.amazon.in")
         self.loc = HOME

    def go_to_mx_player_tab(self):
        locator = self.loc["mx_player_tab"]
        self.page.locator(locator).click()

    def go_to_fashion_tab(self):
        locator = self.loc["amazon_pay_link"]
        self.page.locator(locator).first.click()

# parameterized method to click on any link on homepage
    def go_to_tab(self,text):
        selector = self.loc.get(text)
        if selector:
            self.page.locator(selector).first.click()
            self.page.go_back()
        else:
            raise ValueError(f"Tab '{text}' not found in locators")