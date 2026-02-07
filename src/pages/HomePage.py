from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
         self.page = page
         page.goto("https://www.amazon.in")

    def go_to_mx_player_tab(self):
        self.page.get_by_text("MX Player").click()

    def go_to_fashion_tab(self):
        self.page.get_by_text("Amazon Pay").click()
        
    