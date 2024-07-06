from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_all_clear(calc_page):
    calc_page.fill_first_number(5)
    calc_page.fill_second_number(5)
    calc_page.click_button("add")
    calc_page.click_button("ac")
    assert calc_page.get_first_number() == "0"
    assert calc_page.get_second_number() == "0"
    assert calc_page.get_result() == "Result: No result yet"