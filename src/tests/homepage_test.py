from pages.HomePage import HomePage
from playwright.sync_api import Page

def test_homepage_navigation(page:Page):
    home_page = HomePage(page)
    home_page.go_to_mx_player_tab()
    assert page.title() == "Amazon miniTV - Watch Free Web Series, Movies, Short Films & K-Dramas Online"
