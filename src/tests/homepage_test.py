from pages.HomePage import HomePage
from pages.GFGHomePage import GFGHomePage
from playwright.sync_api import Page

import pytest


# This will run 4 test cases for test_multiple_link case with different link text as parameter and click on that link on homepage
def test_homepage_navigation(page:Page):
    home_page = HomePage(page)
    home_page.go_to_mx_player_tab()
    assert page.title() == "Amazon miniTV - Watch Free Web Series, Movies, Short Films & K-Dramas Online"


def test_homepage_navigation_2(page:Page):
    home_page = HomePage(page)
    home_page.go_to_fashion_tab()


@pytest.mark.parametrize(
    "link",[
        "mx_player_tab",
        "amazon_pay_link",
        "gift_cards"
    ]
)
def test_multiple_link(page:Page,link):
        amazon_home = HomePage(page)
        amazon_home.go_to_tab(link)


def test_gfg(page:Page):
    gfg_home =  GFGHomePage(page)
    gfg_home.open_home_page_gfg()
    gfg_home.seach_text_on_home_page()



@pytest.mark.parametrize(
    "links",[(
        "mx_player_tab",
        "amazon_pay_link",
        "gift_cards"
    )]
)
def test_multiple_link_in_same_test(page:Page,links):
        amazon_home = HomePage(page)
        for l in links:
            amazon_home.go_to_tab(l)
       
