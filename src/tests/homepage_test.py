from pages.HomePage import HomePage
from pages.GFGHomePage import GFGHomePage
from playwright.sync_api import Page

def test_homepage_navigation(page:Page):
    home_page = HomePage(page)
    home_page.go_to_mx_player_tab()
    assert page.title() == "Amazon miniTV - Watch Free Web Series, Movies, Short Films & K-Dramas Online"


def test_homepage_navigation_2(page:Page):
    home_page = HomePage(page)
    home_page.go_to_fashion_tab()


def test_gfg(page:Page):
    gfg_home =  GFGHomePage(page)
    gfg_home.open_home_page_gfg()
    gfg_home.seach_text_on_home_page()