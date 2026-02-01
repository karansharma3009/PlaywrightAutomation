import pytest
from playwright.sync_api import sync_playwright,Page,Browser

@pytest.fixture(scope="function")
def page(browser:Browser):
   context= browser.new_context(
      record_video_dir="video/"
   )
   page = context.new_page()
   yield page
   context.close()


def test_recording_video(page:Page):
    page.goto("https://www.amazon.in")
    page.get_by_text("MX Player").click()
   


# way 2 here we are using get_browser_recording so fixture name should match here. 

@pytest.fixture(scope="function")
def get_browser_recording(browser:Browser):
   context= browser.new_context(
      record_video_dir="video/"
   )
   page = context.new_page()
   yield page
   context.close()


def test_recording_video_2(get_browser_recording: Page):
    get_browser_recording.goto("https://www.amazon.in")
    get_browser_recording.get_by_text("MX Player").click()


# way 3 - use autouse in fixture name to be used by all functions by defualt 
