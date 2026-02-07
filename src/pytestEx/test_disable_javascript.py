from playwright.sync_api import sync_playwright,Page,Route , Browser
import pytest

var_type = ("img","font","stylesheet") # resource types to be blocked


def skip_route_method(route:Route):
    if route.request.resource_type in var_type:
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)
def skip_resource(page:Page):
    page.route("**",skip_route_method)


@pytest.fixture(autouse=True)
def browser_context_args(browser:Browser): # special fixture name to modify browser context args
    return {
        "java_script_enabled": False
    }

# def test_disable_media(page: Page):
#     page.goto("https://www.playwright.dev/docs/intro")
#     title = page.title()
#     page.pause()

def test_disable_javascript(page: Page):
    page.goto("https://www.playwright.dev/docs/intro")
    title = page.title()
    #page.pause()
    