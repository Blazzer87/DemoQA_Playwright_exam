import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo = 500)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://vdcs3tst:Co_ZLHb5ao@192.168.100.17:4003/auth/realms/qpd/protocol/openid-connect/auth?client_id=vdcs3&redirect_uri=https%3A%2F%2F192.168.100.17%3A4003%2Fvendors&response_type=code&scope=openid")
    page.get_by_role("textbox", name="Username or email").fill("vdcs3tst")
    page.get_by_role("textbox", name="Password").fill("Co_ZLHb5ao")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("menuitem", name="ellipsis").click()
    page.get_by_role("menuitem", name="Kinds").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
