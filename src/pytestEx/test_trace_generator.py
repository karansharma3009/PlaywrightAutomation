import pytest
from playwright.sync_api import BrowserContext,Page,Browser


@pytest.fixture(autouse=True)
def trace_test(context : BrowserContext):
    context.tracing.start(
        name="trace",
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield
    context.tracing.stop(path="trace.zip")


def test_method(page: Page):
    page.goto("https://www.amazon.in")
    page.get_by_text("MX Player").click()
