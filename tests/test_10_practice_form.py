import pytest

from tests.base_test import BaseTest


# @pytest.mark.usefixtures('page')
def test_10(page):
    page.goto("https://demoqa.com/automation-practice-form", wait_until='domcontentloaded', timeout=60000)
    print(page.title())



class TestPage10PracticeForm(BaseTest):

    def test_10_practice_form(self):
        pass
