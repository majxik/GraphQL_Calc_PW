import pytest
from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage
from query_page import QueryPage

#Author: Martin Maiksnar
#This is a fixture for the calculator page

@pytest.fixture
def calc_page():
    with sync_playwright() as p:
        # For debuging, you can set headless=False, slow_mo=100
        browser = p.chromium.launch()
        page = browser.new_page()
        calc_page = CalculatorPage(page)
        calc_page.open()
        yield calc_page  
        browser.close()

@pytest.fixture
def query_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        query_page = QueryPage(page)
        query_page.navigate()
        yield query_page
        browser.close()