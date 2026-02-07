from playwright.sync_api  import Page
from .locators import GFG
class GFGHomePage:

    def __init__(self,page:Page):
        self.page =page
        self.loc = GFG

    def open_home_page_gfg(self):
        self.page.goto("https://www.geeksforgeeks.org")

    def seach_text_on_home_page(self):
        self.page.goto("https://www.geeksforgeeks.org")
        locator = self.loc["search_input"]
        self.page.locator(locator).type("playwright")

        
        