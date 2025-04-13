import pytest
from playwright.sync_api import Playwright, Page, Browser


@pytest.fixture(autouse=True, scope='session', params=["chromium", "firefox", "webkit"])
def browser(request, playwright: Playwright):
    browser_type = request.param
    browser: Browser = getattr(playwright, browser_type).launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

