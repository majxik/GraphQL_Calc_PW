from playwright.sync_api import sync_playwright
from calculator_page import CalculatorPage

#Author: Martin Maiksnar

def test_all_clear(calc_page):
    calc_page.fill_first_number(5)
    calc_page.fill_second_number(5)
    calc_page.click_add()
    calc_page.click_ac()
    result = calc_page.get_result()
    print("The result is:", result)
    assert result == "Result: No result yet"