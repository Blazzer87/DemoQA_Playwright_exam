import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.fixture(autouse=True, scope="function", params=["chromium", "firefox", "webkit"])
def page2(request, playwright: Playwright):


        browser_type = request.param

        browser = getattr(playwright, browser_type).launch(headless=False, slow_mo=500, timeout=60000)

        # создает изолированный сеанс браузера (новый объект окна браузера)
        context = browser.new_context()

        # создает страницу браузера в рамках этого изолированного сеанса
        page2 = context.new_page()

        yield page2

        context.close()
        browser.close()


def test_2(page2):

        # передаёт в страницу какой урл нам необходимо открыть
        page2.goto("https://demoqa.com/text-box", wait_until='domcontentloaded')
        # где wait_until='domcontentloaded' - один из вариантов ожидания ранней загрузки страницы

        # действие передачи текста по объекту который найден через РОЛЬ
        page2.get_by_role("textbox", name="Full Name").fill("Sergey")

        # действие передачи текста по объекту который найден через ЛОКАТОР
        page2.locator("#permanentAddress").fill("и тут тоже какой то адрес")

        # действие передачи нажатия клавиши в объект который найден через ЛОКАТОР
        page2.locator("#permanentAddress").press("Enter")


        page2.get_by_role("textbox", name="Current Address").fill("павапвап")
        page2.locator("#permanentAddress").fill("павп")
        page2.get_by_role("textbox", name="Full Name").fill("апыапывап")
        page2.get_by_role("textbox", name="name@example.com").fill("sdfgsdfgdsf")

