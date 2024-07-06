import pytest
from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage
from query_page import QueryPage

#Author: Martin Maiksnar
#This is a fixture for the calculator page & query page

import pytest
from playwright.sync_api import sync_playwright

# Generic fixture to manage browser context
@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

# Calc_page fixture using the browser_context fixture
@pytest.fixture
def calc_page(browser_context):
    page = browser_context.new_page()
    calc_page = CalculatorPage(page)
    calc_page.open()
    yield calc_page

# Query_page fixture using the browser_context fixture
@pytest.fixture
def query_page(browser_context):
    page = browser_context.new_page()
    query_page = QueryPage(page)
    query_page.navigate()
    yield query_page