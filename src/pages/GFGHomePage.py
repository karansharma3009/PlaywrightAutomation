from playwright.sync_api  import Page

class GFGHomePage:

    def __init__(self,page:Page):
        self.page =page

    def open_home_page_gfg(self):
        self.page.goto("https://www.geeksforgeeks.org/")

    def seach_text_on_home_page(self):
        self.page.locator("input.HomePageSearchContainer_homePageSearchContainer_container_input__1LS0r").type("playwright")

        
        